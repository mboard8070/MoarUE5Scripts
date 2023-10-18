import unreal

# The path to your Blueprint (the 'C' at the end is important as it signifies the Blueprint's generated class)
blueprint_path = '/Game/StarterContent/Blueprints/Blueprint_WallSconce.Blueprint_WallSconce_C'


def spawn_actor_from_blueprint():
    # Load the Blueprint class
    blueprint_class = unreal.load_class(None, blueprint_path)

    if blueprint_class is None:
        unreal.log_error("Failed to load the Blueprint.")
        return

    # Get all viewport clients
    all_viewport_clients = unreal.EditorViewportLibrary.get_all_viewport_clients()
    if not all_viewport_clients:
        unreal.log_error("No viewport clients are available.")
        return

    # We're assuming here the first client is the one you're interested in
    viewport_client = all_viewport_clients[0]

    # Now we get the camera location and rotation from the viewport client
    camera_location = viewport_client.get_view_location()
    camera_rotation = viewport_client.get_view_rotation()

    # Spawn the Blueprint actor from the class at the camera location with the camera rotation
    spawned_actor = unreal.EditorLevelLibrary.spawn_actor_from_class(blueprint_class, camera_location, camera_rotation)

    if spawned_actor is not None:
        unreal.log(f"Spawned {spawned_actor.get_name()} at {camera_location}")
    else:
        unreal.log_error("Failed to spawn actor.")


# Execute the function
spawn_actor_from_blueprint()
