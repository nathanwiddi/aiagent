import os

def get_files_info(working_directory, directory=None):
    try:
        if directory is None:
            directory = working_directory

        abs_working_directory = os.path.abspath(working_directory)
        abs_directory = os.path.abspath(directory)

        if not os.path.isdir(abs_directory):
            return f'Error: \"{directory}\" is not a directory'

        lines = []
        for entry in os.listdir(abs_directory):
            entry_path = os.path.join(abs_directory, entry)
            is_directory = os.path.isdir(entry_path)
            size = os.path.getsize(entry_path)  # Applies to both files and directories
            lines.append(f"- {entry}: file_size={size} bytes, is_dir={is_directory}")

        return "\n".join(lines)

    except Exception as e:
        return f"Error: {e}"
