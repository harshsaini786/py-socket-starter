import socket

def main():
      # Create a TCP/IP socket
      sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

      # Connect the socket to the port where the server is listening
      server_address = ('localhost', 8000)
      print('connecting to {} port {}'.format(*server_address))
      sock.connect(server_address)

      try:
            # Send data
            message = b'This is the message.  It will be repeated.'
            print('sending {!r}'.format(message))
            sock.sendall(message)

            # Look for the response
            amount_received = ""
            while True:
                  data = sock.recv(16)
                  amount_received += data.decode("utf-8")
                  print('received {!r}'.format(data))
                  if len(amount_received) == len(message):
                        break
            print(amount_received)
      except:
            print("Error")
      finally:
            print('closing socket')
            sock.close()



if __name__ == "__main__":
      main()