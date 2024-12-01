from cerebrum.manager.tool import ToolManager

import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Upload tools")
    parser.add_argument(
        "--tool_path",
        required=True
    )
    args = parser.parse_args()

    manager = ToolManager('https://aios.foundation')

    tool_package = manager.package_tool(args.tool_path)

    manager.upload_tool(tool_package)