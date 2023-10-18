import unreal

editor_util = unreal.EditorUtilityLibrary()

def rename_selected_assets(prefix="Asset_"):
    # Get the currently selected assets in the content browser
    selected_assets = editor_util.get_selected_assets()

    if not selected_assets:
        print("No assets selected. Please select assets in the Content Browser to rename.")
        return

    for index, asset in enumerate(selected_assets):
        # Extract the current asset path and name
        current_path = asset.get_path_name()
        current_directory = current_path.rsplit('/', 1)[0]  # Split the string by last occurrence of '/' and get first part

        # Create a new name based on the prefix and the index
        new_name = f"{prefix}{index:03d}"  # This will result in names like Asset_000, Asset_001, etc.

        # Construct the new full path with the new name
        new_path = f"{current_directory}/{new_name}"

        # Rename the asset
        try:
            # Attempt to rename the asset using the full paths
            unreal.EditorAssetLibrary.rename_asset(current_path, new_path)
        except Exception as e:
            # If an error occurs, log the message and continue to the next asset
            print(f"Failed to rename {current_path} to {new_path}. Error: {str(e)}")
            continue  # Skip to the next asset

    print(f"Renamed {len(selected_assets)} assets.")

# Use the function with a custom prefix
rename_selected_assets("MyCustomAsset_")
