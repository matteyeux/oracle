#!/usr/bin/env python3
"""Main code for the oracle API."""
import argparse
import uvicorn


def parse_arguments() -> argparse.Namespace:
    """Parse arguments from cmdline to initialize
    optional settings such as port or reload.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-H",
        "--host",
        type=str,
        dest="host",
        default="127.0.0.1",
        help="specify host",
    )
    parser.add_argument(
        "-p",
        "--port",
        type=int,
        dest="port",
        default=5555,
        help="specify port",
    )
    parser.add_argument(
        "-d",
        "--debug",
        action="store_true",
        default=False,
        help="debug mode",
    )
    parser.add_argument(
        "-r",
        "--reload",
        action="store_true",
        default=False,
        help="autoreload",
    )
    return parser.parse_args()


def main() -> int:
    """Main function which will run the uvicorn
    web server and run the API from app.py."""
    parser = parse_arguments()

    uvicorn.run(
        "oracle.app:app",
        host=parser.host,
        port=parser.port,
        reload=parser.reload,
    )

    return 0


if __name__ == "__main__":
    main()
