import os

MAX_CHARS_TO_READ = 10000

def get_file_content(working_directory: str, file_path: str) -> str:
    try:
        abs_working_dir = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(abs_working_dir, file_path))
        if os.path.commonpath([abs_working_dir, target_dir]) != abs_working_dir:
            return f'Error: Cannot list "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(target_dir):
            f'Error: File not found or is not a regular file: "{file_path}"'

        with open(target_dir, "r") as f:
            file_content = f.read(MAX_CHARS_TO_READ)
            if f.read(1):
                file_content += f'[...File "{file_path}" truncated at {MAX_CHARS_TO_READ} characters]'

        return file_content

    except Exception as e:
        return f"Error listing files: {e}"
    


schema_get_files_content = {
    "type": "function",
    "function": {
        "name": "get_file_content",
        "description": "Gives the contents of a file, truncated to 10000 characters",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Path to the file, whose content is to be read, relative to the working directory.",
                },
            },
        },
    },
}