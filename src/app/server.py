# server.py
# Copyright 2024, 2025 Michael Konrad 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Adapted from Sling Academy

import asyncio

# Define a protocol class that inherits from asyncio.Protocol
class HTTPProtocol(asyncio.Protocol):
    # This method is called when a new connection is established
    def connection_made(self, transport):
        # Save a reference to the transport object
        self.transport = transport

    # This method is called when data is received from the client
    def data_received(self, data):
        # Parse the HTTP request line
        request_line = data.split(b"\r\n", 1)[0]
        method, path, version = request_line.split(b" ", 3)
        # Print a message on the server side
        print(f"Request: {method.decode()} {path.decode()} {version.decode()}")
        # Check if the method is GET and the path is /
        if method == b"GET" and path == b"/":
            response = (
                'HTTP/1.1 200 OK\r\n'
                'Content-Type: text/plain\r\n'
                '\r\n'
                'Container ready to install Python packages.'
            )
            # Encode the response from string to bytes
            response_data = response.encode()
            # Send the HTTP response to the client
            self.transport.write(response_data)
        else:
            # Send a 404 Not Found response to the client
            self.transport.write(b"HTTP/1.1 404 Not Found\r\n\r\n")
        # Close the connection
        self.transport.close()


# Define an async function that creates and runs the server
async def main():
    # Get the current event loop
    loop = asyncio.get_running_loop()
    # Create the server using asyncio.create_server()
    server = await loop.create_server(
        HTTPProtocol,  # The protocol factory
        "0.0.0.0",  # The host address
        8080,  # The port number
    )

    # Get the server address and port
    addr = server.sockets[0].getsockname()
    # Print a message on the server side
    print(f"Serving on http://{addr[0]}:{addr[1]}")

    # Run the server until it is stopped
    async with server:
        await server.serve_forever()


# Run the async function using asyncio.run()
asyncio.run(main())