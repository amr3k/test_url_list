"""
### Source: https://stackoverflow.com/a/57689101/7301680
"""


async def fetch_html(url, session) -> tuple:
    try:
        resp = await session.request(method="GET", url=url)
    except InvalidURL:
        print(f"Invalid URL: {url}")  # Delete this line if you want to show only working URLs
        pass
    except Exception:  # Any other exceptions like connection error, Or disconnected server
        pass
    else:
        return (url, resp.status)


async def make_requests(urls: set) -> None:
    async with ClientSession() as session:
        tasks = []
        for url in urls:
            tasks.append(
                fetch_html(url=url, session=session)
            )
        results = await asyncio.gather(*tasks)

    for result in results:
        try:
            print(f'{result[1]} \t {str(result[0])}')
        except TypeError:
            pass

if __name__ == "__main__":
    try:
        import pathlib
        import sys
        import asyncio
        import aiohttp
        from aiohttp import ClientSession, ClientConnectorError, InvalidURL
    except (ModuleNotFoundError, NameError):
        print("Please install missing modules with `pip install -r requirements.txt`")
    try:
        assert sys.version_info >= (3, 7)
    except AssertionError:
        print("This script requires python version 3.7 or higher")
        sys.exit(1)
    here = pathlib.Path(__file__).parent
    try:
        with open(here.joinpath(sys.argv[1])) as infile:
            urls = set(map(str.strip, infile))
    except IndexError:
        print(f"Usage:\t{sys.argv[0]} url_file")
        sys.exit(0)
    except FileNotFoundError:
        print("File Not found")
        sys.exit(1)
    else:
        asyncio.run(make_requests(urls=urls))
