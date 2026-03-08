# dart:io library

File, socket, HTTP, and other I/O support for non-web applications.

**Important:** Browser-based apps can't use this library.
Only the following can import and use the dart:io library:

- Servers
- Command-line scripts
- Flutter mobile apps
- Flutter desktop apps


This library allows you to work with files, directories,
sockets, processes, HTTP servers and clients, and more.
Many operations related to input and output are asynchronous
and are handled using [Future](flutter-docs://api/dart-async/Future) s or [Stream](flutter-docs://api/dart-async/Stream) s, both of which
are defined in the [Omitted link: dart:async library].

To use the dart:io library in your code:

```dart
import 'dart:io';

```
For an introduction to I/O in Dart, see the [dart:io library tour](https://dart.dev/guides/libraries/library-tour#dartio).

## File, Directory, and Link

An instance of [File](flutter-docs://api/dart-io/File), [Directory](flutter-docs://api/dart-io/Directory), or [Link](flutter-docs://api/dart-io/Link) represents a file,
directory, or link, respectively, in the native file system.

You can manipulate the file system through objects of these types.
For example, you can rename a file or directory:

```dart
File myFile = File('myFile.txt');
myFile.rename('yourFile.txt').then((_) => print('file renamed'));

```
Many methods provided by the [File](flutter-docs://api/dart-io/File), [Directory](flutter-docs://api/dart-io/Directory), and [Link](flutter-docs://api/dart-io/Link) classes
run asynchronously and return a [Future](flutter-docs://api/dart-async/Future).

## FileSystemEntity

[File](flutter-docs://api/dart-io/File), [Directory](flutter-docs://api/dart-io/Directory), and [Link](flutter-docs://api/dart-io/Link) all extend [FileSystemEntity](flutter-docs://api/dart-io/FileSystemEntity).
In addition to being the superclass for these classes,
FileSystemEntity has a number of static methods for working with paths.

To get information about a path,
you can use the [FileSystemEntity](flutter-docs://api/dart-io/FileSystemEntity) static methods
such as [FileSystemEntity.isDirectory](flutter-docs://api/dart-io/FileSystemEntity/isDirectory), [FileSystemEntity.isFile](flutter-docs://api/dart-io/FileSystemEntity/isFile),
and [FileSystemEntity.exists](flutter-docs://api/dart-io/FileSystemEntity/exists).
Because file system access involves I/O, these methods
are asynchronous and return a [Future](flutter-docs://api/dart-async/Future).

```dart
FileSystemEntity.isDirectory(myPath).then((isDir) {
  if (isDir) {
    print('$myPath is a directory');
  } else {
    print('$myPath is not a directory');
  }
});

```


## HttpServer and HttpClient

The classes [HttpClient](flutter-docs://api/dart-io/HttpClient) and [HttpServer](flutter-docs://api/dart-io/HttpServer) provide low-level HTTP
functionality.

Instead of using these classes directly, consider using more
developer-friendly and composable APIs found in packages.

For HTTP clients, look at [`package:http`](https://pub.dev/packages/http).

For HTTP servers, look at [Write HTTP servers](https://dart.dev/tutorials/server/httpserver) on [dart.dev](https://dart.dev/).

## Process

The [Process](flutter-docs://api/dart-io/Process) class provides a way to run a process on
the native machine.
For example, the following code spawns a process that recursively lists
the files under `web`.

```dart
Process.start('ls', ['-R', 'web']).then((process) {
  stdout.addStream(process.stdout);
  stderr.addStream(process.stderr);
  process.exitCode.then(print);
});

```
Using [Process.start](flutter-docs://api/dart-io/Process/start) returns a [Future](flutter-docs://api/dart-async/Future),
which completes with a [Process](flutter-docs://api/dart-io/Process) object when the process has started.
This [Process](flutter-docs://api/dart-io/Process) object allows you to interact
with the process while it is running.
Using [Process.run](flutter-docs://api/dart-io/Process/run) returns a [Future](flutter-docs://api/dart-async/Future),
which completes with a [ProcessResult](flutter-docs://api/dart-io/ProcessResult) object when the spawned process has
terminated. This [ProcessResult](flutter-docs://api/dart-io/ProcessResult) object collects the output and exit code
from the process.

When using [Process.start](flutter-docs://api/dart-io/Process/start),
you need to read all data coming on the [Process.stdout](flutter-docs://api/dart-io/Process/stdout) and [Process.stderr](flutter-docs://api/dart-io/Process/stderr) streams, otherwise the system resources will not be freed.

## WebSocket

The [WebSocket](flutter-docs://api/dart-io/WebSocket) class provides support for the web socket protocol. This
allows full-duplex communications between client and server applications.

A web socket server uses a normal HTTP server for accepting web socket
connections. The initial handshake is a HTTP request which is then upgraded to a
web socket connection.
The server upgrades the request using [WebSocketTransformer](flutter-docs://api/dart-io/WebSocketTransformer) and listens for the data on the returned web socket.
For example, here's a mini server that listens for 'ws' data
on a WebSocket:

```dart
runZoned(() async {
  var server = await HttpServer.bind('127.0.0.1', 4040);
  server.listen((HttpRequest req) async {
    if (req.uri.path == '/ws') {
      var socket = await WebSocketTransformer.upgrade(req);
      socket.listen(handleMsg);
    }
  });
}, onError: (e) => print("An error occurred."));

```
The client connects to the [WebSocket](flutter-docs://api/dart-io/WebSocket) using the [WebSocket.connect](flutter-docs://api/dart-io/WebSocket/connect) method
and a URI that uses the Web Socket protocol.
The client can write to the [WebSocket](flutter-docs://api/dart-io/WebSocket) with the [WebSocket.add](flutter-docs://api/dart-io/WebSocket/add) method.
For example,

```dart
var socket = await WebSocket.connect('ws://127.0.0.1:4040/ws');
socket.add('Hello, World!');

```
Check out the [websocket_sample](https://github.com/dart-lang/dart-samples/tree/master/html5/web/websockets/basics) app, which uses [WebSocket](flutter-docs://api/dart-io/WebSocket) s to communicate with a server.

## Socket and ServerSocket

Clients and servers use [Socket](flutter-docs://api/dart-io/Socket) s to communicate using the TCP protocol.
Use [ServerSocket](flutter-docs://api/dart-io/ServerSocket) on the server side and [Socket](flutter-docs://api/dart-io/Socket) on the client.
The server creates a listening socket using the `bind()` method and
then listens for incoming connections on the socket. For example:

```dart
ServerSocket.bind('127.0.0.1', 4041)
  .then((serverSocket) {
    serverSocket.listen((socket) {
      socket.transform(utf8.decoder).listen(print);
    });
  });

```
A client connects a [Socket](flutter-docs://api/dart-io/Socket) using the `connect()` method,
which returns a [Future](flutter-docs://api/dart-async/Future).
Using `write()`, `writeln()`, or `writeAll()` are the easiest ways to
send data over the socket.
For example:

```dart
Socket.connect('127.0.0.1', 4041).then((socket) {
  socket.write('Hello, World!');
});

```
Besides [Socket](flutter-docs://api/dart-io/Socket) and [ServerSocket](flutter-docs://api/dart-io/ServerSocket), the [RawSocket](flutter-docs://api/dart-io/RawSocket) and [RawServerSocket](flutter-docs://api/dart-io/RawServerSocket) classes are available for lower-level access
to async socket IO.

## Standard output, error, and input streams

This library provides the standard output, error, and input
streams, named [stdout](flutter-docs://api/dart-io/stdout), [stderr](flutter-docs://api/dart-io/stderr), and [stdin](flutter-docs://api/dart-io/stdin), respectively.

The [stdout](flutter-docs://api/dart-io/stdout) and [stderr](flutter-docs://api/dart-io/stderr) streams are both [IOSink](flutter-docs://api/dart-io/IOSink) s and have the same set
of methods and properties.

To write a string to [stdout](flutter-docs://api/dart-io/stdout):

```dart
stdout.writeln('Hello, World!');

```
To write a list of objects to [stderr](flutter-docs://api/dart-io/stderr):

```dart
stderr.writeAll([ 'That ', 'is ', 'an ', 'error.', '\n']);

```
The standard input stream is a true [Stream](flutter-docs://api/dart-async/Stream), so it inherits
properties and methods from the [Stream](flutter-docs://api/dart-async/Stream) class.

To read text synchronously from the command line
(the program blocks waiting for user to type information):

```dart
String? inputText = stdin.readLineSync();

```


## Classes

[BytesBuilder](flutter-docs://api/dart-typed_data/BytesBuilder)
Builds a list of bytes, allowing bytes and lists of bytes to be added at the
end.

[CompressionOptions](flutter-docs://api/dart-io/CompressionOptions)
Options controlling compression in a [WebSocket](flutter-docs://api/dart-io/WebSocket).

[ConnectionTask](flutter-docs://api/dart-io/ConnectionTask)<S>
A cancelable connection attempt.

[ContentType](flutter-docs://api/dart-io/ContentType)
A MIME/IANA media type used as the value of the
[HttpHeaders.contentTypeHeader](flutter-docs://api/dart-io/HttpHeaders/contentTypeHeader) header.

[Cookie](flutter-docs://api/dart-io/Cookie)
Representation of a cookie. For cookies received by the server as Cookie
header values only [name](flutter-docs://api/dart-io/Cookie/name) and [value](flutter-docs://api/dart-io/Cookie/value) properties will be set. When building a
cookie for the 'set-cookie' header in the server and when receiving cookies
in the client as 'set-cookie' headers all fields can be used.

[Datagram](flutter-docs://api/dart-io/Datagram)
A data packet received by a [RawDatagramSocket](flutter-docs://api/dart-io/RawDatagramSocket).

[Directory](flutter-docs://api/dart-io/Directory)
A reference to a directory (or *folder*) on the file system.

[File](flutter-docs://api/dart-io/File)
A reference to a file on the file system.

[FileLock](flutter-docs://api/dart-io/FileLock)
Type of lock when requesting a lock on a file.

[FileMode](flutter-docs://api/dart-io/FileMode)
The modes in which a [File](flutter-docs://api/dart-io/File) can be opened.

[FileStat](flutter-docs://api/dart-io/FileStat)
The result of calling the POSIX `stat()` function on a file system object.

[FileSystemCreateEvent](flutter-docs://api/dart-io/FileSystemCreateEvent)
File system event for newly created file system objects.

[FileSystemDeleteEvent](flutter-docs://api/dart-io/FileSystemDeleteEvent)
File system event for deletion of file system objects.

[FileSystemEntity](flutter-docs://api/dart-io/FileSystemEntity)
The common superclass of [File](flutter-docs://api/dart-io/File), [Directory](flutter-docs://api/dart-io/Directory), and [Link](flutter-docs://api/dart-io/Link).

[FileSystemEntityType](flutter-docs://api/dart-io/FileSystemEntityType)
The type of an entity on the file system,
such as a file, directory, or link.

[FileSystemEvent](flutter-docs://api/dart-io/FileSystemEvent)
Base event class emitted by [FileSystemEntity.watch](flutter-docs://api/dart-io/FileSystemEntity/watch).

[FileSystemModifyEvent](flutter-docs://api/dart-io/FileSystemModifyEvent)
File system event for modifications of file system objects.

[FileSystemMoveEvent](flutter-docs://api/dart-io/FileSystemMoveEvent)
File system event for moving of file system objects.

[GZipCodec](flutter-docs://api/dart-io/GZipCodec)
The [GZipCodec](flutter-docs://api/dart-io/GZipCodec) encodes raw bytes to GZip compressed bytes and decodes GZip
compressed bytes to raw bytes.

[HeaderValue](flutter-docs://api/dart-io/HeaderValue)
Representation of a header value in the form:

[HttpClient](flutter-docs://api/dart-io/HttpClient)
An HTTP client for communicating with an HTTP server.

[HttpClientBasicCredentials](flutter-docs://api/dart-io/HttpClientBasicCredentials)
Represents credentials for basic authentication.

[HttpClientBearerCredentials](flutter-docs://api/dart-io/HttpClientBearerCredentials)
Represents credentials for bearer token authentication.

[HttpClientCredentials](flutter-docs://api/dart-io/HttpClientCredentials)
Represents credentials for authentication in [HttpClient](flutter-docs://api/dart-io/HttpClient).

[HttpClientDigestCredentials](flutter-docs://api/dart-io/HttpClientDigestCredentials)
Represents credentials for digest authentication.

[HttpClientRequest](flutter-docs://api/dart-io/HttpClientRequest)
HTTP request for a client connection.

[HttpClientResponse](flutter-docs://api/foundation/HttpClientResponse)
HTTP response for a client connection.

[HttpConnectionInfo](flutter-docs://api/dart-io/HttpConnectionInfo)
Information about an [HttpRequest](flutter-docs://api/dart-io/HttpRequest), [HttpResponse](flutter-docs://api/dart-io/HttpResponse), [HttpClientRequest](flutter-docs://api/dart-io/HttpClientRequest), or
[HttpClientResponse](flutter-docs://api/foundation/HttpClientResponse) connection.

[HttpConnectionsInfo](flutter-docs://api/dart-io/HttpConnectionsInfo)
Summary statistics about an [HttpServer](flutter-docs://api/dart-io/HttpServer) s current socket connections.

[HttpDate](flutter-docs://api/dart-io/HttpDate)
Utility functions for working with dates with HTTP specific date
formats.

[HttpHeaders](flutter-docs://api/dart-io/HttpHeaders)
Headers for HTTP requests and responses.

[HttpOverrides](flutter-docs://api/dart-io/HttpOverrides)
This class facilitates overriding [HttpClient](flutter-docs://api/dart-io/HttpClient) with a mock implementation.
It should be extended by another class in client code with overrides
that construct a mock implementation. The implementation in this base class
defaults to the actual [HttpClient](flutter-docs://api/dart-io/HttpClient) implementation. For example:

[HttpRequest](flutter-docs://api/dart-io/HttpRequest)
A server-side object
that contains the content of and information about an HTTP request.

[HttpResponse](flutter-docs://api/dart-io/HttpResponse)
An HTTP response, which returns the headers and data
from the server to the client in response to an HTTP request.

[HttpServer](flutter-docs://api/dart-io/HttpServer)
A server that delivers content, such as web pages, using the HTTP protocol.

[HttpSession](flutter-docs://api/dart-io/HttpSession)
The [HttpRequest.session](flutter-docs://api/dart-io/HttpRequest/session) of an [HttpRequest](flutter-docs://api/dart-io/HttpRequest).

[HttpStatus](flutter-docs://api/dart-html/HttpStatus)
HTTP status codes. Exported in dart:io and dart:html.

[InternetAddress](flutter-docs://api/dart-io/InternetAddress)
An internet address or a Unix domain address.

[InternetAddressType](flutter-docs://api/dart-io/InternetAddressType)
The type, or address family, of an [InternetAddress](flutter-docs://api/dart-io/InternetAddress).

[IOOverrides](flutter-docs://api/dart-io/IOOverrides)
Facilities for overriding various APIs of `dart:io` with mock
implementations.

[IOSink](flutter-docs://api/dart-io/IOSink)
A combined byte and text output.

[Link](flutter-docs://api/dart-io/Link)
References to filesystem links.

[NetworkInterface](flutter-docs://api/dart-io/NetworkInterface)
A [NetworkInterface](flutter-docs://api/dart-io/NetworkInterface) represents an active network interface on the current
system. It contains a list of [InternetAddress](flutter-docs://api/dart-io/InternetAddress) es that are bound to the
interface.

[Pipe](flutter-docs://api/dart-io/Pipe)
An anonymous pipe that can be used to send data in a single direction i.e.
data written to [write](flutter-docs://api/dart-io/Pipe/write) can be read using [read](flutter-docs://api/dart-io/Pipe/read).

[Platform](flutter-docs://api/dart-io/Platform)
Information about the environment in which the current program is running.

[Process](flutter-docs://api/dart-io/Process)
The means to execute a program.

[ProcessInfo](flutter-docs://api/dart-io/ProcessInfo)
Methods for retrieving information about the current process.

[ProcessResult](flutter-docs://api/dart-io/ProcessResult)
The result of running a non-interactive
process started with [Process.run](flutter-docs://api/dart-io/Process/run) or [Process.runSync](flutter-docs://api/dart-io/Process/runSync).

[ProcessSignal](flutter-docs://api/dart-io/ProcessSignal)
On Posix systems, [ProcessSignal](flutter-docs://api/dart-io/ProcessSignal) is used to send a specific signal
to a child process, see `Process.kill`.

[ProcessStartMode](flutter-docs://api/dart-io/ProcessStartMode)
Modes for running a new process.

[RandomAccessFile](flutter-docs://api/dart-io/RandomAccessFile)
Random access to the data in a file.

[RawDatagramSocket](flutter-docs://api/dart-io/RawDatagramSocket)
An unbuffered interface to a UDP socket.

[RawSecureServerSocket](flutter-docs://api/dart-io/RawSecureServerSocket)
A server socket providing a stream of low-level [RawSecureSocket](flutter-docs://api/dart-io/RawSecureSocket) s.

[RawSecureSocket](flutter-docs://api/dart-io/RawSecureSocket)
`RawSecureSocket` provides a secure (SSL or TLS) network connection.

[RawServerSocket](flutter-docs://api/dart-io/RawServerSocket)
A listening socket.

[RawSocket](flutter-docs://api/dart-io/RawSocket)
A TCP connection.

[RawSocketEvent](flutter-docs://api/dart-io/RawSocketEvent)
Events for the [RawDatagramSocket](flutter-docs://api/dart-io/RawDatagramSocket), [RawSecureSocket](flutter-docs://api/dart-io/RawSecureSocket), and [RawSocket](flutter-docs://api/dart-io/RawSocket).

[RawSocketOption](flutter-docs://api/dart-io/RawSocketOption)
The [RawSocketOption](flutter-docs://api/dart-io/RawSocketOption) is used as a parameter to [Socket.setRawOption](flutter-docs://api/dart-io/Socket/setRawOption) and
[RawSocket.setRawOption](flutter-docs://api/dart-io/RawSocket/setRawOption) to customize the behaviour of the underlying
socket.

[RawSynchronousSocket](flutter-docs://api/dart-io/RawSynchronousSocket)
A low-level class for communicating synchronously over a TCP socket.

[RawZLibFilter](flutter-docs://api/dart-io/RawZLibFilter)
The [RawZLibFilter](flutter-docs://api/dart-io/RawZLibFilter) class provides a low-level interface to zlib.

[ReadPipe](flutter-docs://api/dart-io/ReadPipe)
The "read" end of an [Pipe](flutter-docs://api/dart-io/Pipe) created by [Pipe.create](flutter-docs://api/dart-io/Pipe/create).

[RedirectInfo](flutter-docs://api/dart-io/RedirectInfo)
Redirect information.

[ResourceHandle](flutter-docs://api/dart-io/ResourceHandle)
A wrapper around OS resource handle so it can be passed via Socket
as part of [SocketMessage](flutter-docs://api/dart-io/SocketMessage).

[SameSite](flutter-docs://api/dart-io/SameSite)
Cookie cross-site availability configuration.

[SecureServerSocket](flutter-docs://api/dart-io/SecureServerSocket)
A server socket, providing a stream of high-level [Socket](flutter-docs://api/dart-io/Socket) s.

[SecureSocket](flutter-docs://api/dart-io/SecureSocket)
A TCP socket using TLS and SSL.

[SecurityContext](flutter-docs://api/dart-io/SecurityContext)
The object containing the certificates to trust when making
a secure client connection, and the certificate chain and
private key to serve from a secure server.

[ServerSocket](flutter-docs://api/dart-io/ServerSocket)
A listening socket.

[Socket](flutter-docs://api/dart-io/Socket)
A TCP connection between two sockets.

[SocketControlMessage](flutter-docs://api/dart-io/SocketControlMessage)
Control message part of the [SocketMessage](flutter-docs://api/dart-io/SocketMessage) received by a call to
[RawSocket.readMessage](flutter-docs://api/dart-io/RawSocket/readMessage).

[SocketDirection](flutter-docs://api/dart-io/SocketDirection)
The [SocketDirection](flutter-docs://api/dart-io/SocketDirection) is used as a parameter to [Socket.close](flutter-docs://api/dart-io/Socket/close) and
[RawSocket.close](flutter-docs://api/dart-io/RawSocket/close) to close a socket in the specified direction(s).

[SocketMessage](flutter-docs://api/dart-io/SocketMessage)
A socket message received by a [RawDatagramSocket](flutter-docs://api/dart-io/RawDatagramSocket).

[SocketOption](flutter-docs://api/dart-io/SocketOption)
An option for a socket which is configured using [Socket.setOption](flutter-docs://api/dart-io/Socket/setOption).

[Stdin](flutter-docs://api/dart-io/Stdin)
The standard input stream of the process.

[StdioType](flutter-docs://api/dart-io/StdioType)
The type of object a standard IO stream can be attached to.

[Stdout](flutter-docs://api/dart-io/Stdout)
An [IOSink](flutter-docs://api/dart-io/IOSink) connected to either the standard out or error of the process.

[SystemEncoding](flutter-docs://api/dart-io/SystemEncoding)
The system encoding is the current code page on Windows and UTF-8 on Linux
and Mac.

[TlsProtocolVersion](flutter-docs://api/dart-io/TlsProtocolVersion)
A Transport Layer Security (TLS) version.

[WebSocket](flutter-docs://api/dart-io/WebSocket)
A two-way HTTP communication object for client or server applications.

[WebSocketStatus](flutter-docs://api/dart-io/WebSocketStatus)
WebSocket status codes used when closing a WebSocket connection.

[WebSocketTransformer](flutter-docs://api/dart-io/WebSocketTransformer)
The [WebSocketTransformer](flutter-docs://api/dart-io/WebSocketTransformer) provides the ability to upgrade a
[HttpRequest](flutter-docs://api/dart-io/HttpRequest) to a [WebSocket](flutter-docs://api/dart-io/WebSocket) connection. It supports both
upgrading a single [HttpRequest](flutter-docs://api/dart-io/HttpRequest) and upgrading a stream of
[HttpRequest](flutter-docs://api/dart-io/HttpRequest) s.

[WritePipe](flutter-docs://api/dart-io/WritePipe)
The "write" end of an [Pipe](flutter-docs://api/dart-io/Pipe) created by [Pipe.create](flutter-docs://api/dart-io/Pipe/create).

[X509Certificate](flutter-docs://api/dart-io/X509Certificate)
X509Certificate represents an SSL certificate, with accessors to
get the fields of the certificate.

[ZLibCodec](flutter-docs://api/dart-io/ZLibCodec)
The [ZLibCodec](flutter-docs://api/dart-io/ZLibCodec) encodes raw bytes to ZLib compressed bytes and decodes ZLib
compressed bytes to raw bytes.

[ZLibDecoder](flutter-docs://api/dart-io/ZLibDecoder)
The [ZLibDecoder](flutter-docs://api/dart-io/ZLibDecoder) is used by [ZLibCodec](flutter-docs://api/dart-io/ZLibCodec) and [GZipCodec](flutter-docs://api/dart-io/GZipCodec) to decompress data.

[ZLibEncoder](flutter-docs://api/dart-io/ZLibEncoder)
The [ZLibEncoder](flutter-docs://api/dart-io/ZLibEncoder) encoder is used by [ZLibCodec](flutter-docs://api/dart-io/ZLibCodec) and [GZipCodec](flutter-docs://api/dart-io/GZipCodec) to compress
data.

[ZLibOption](flutter-docs://api/dart-io/ZLibOption)
Exposes ZLib options for input parameters.

## Enums

[HttpClientResponseCompressionState](flutter-docs://api/dart-io/HttpClientResponseCompressionState)
Enum that specifies the compression state of the byte stream of an
[HttpClientResponse](flutter-docs://api/foundation/HttpClientResponse).

## Constants

[gzip](flutter-docs://api/dart-io/gzip) → const [GZipCodec](flutter-docs://api/dart-io/GZipCodec)
An instance of the default implementation of the [GZipCodec](flutter-docs://api/dart-io/GZipCodec).

[systemEncoding](flutter-docs://api/dart-io/systemEncoding) → const [SystemEncoding](flutter-docs://api/dart-io/SystemEncoding)
The current system encoding.

[zlib](flutter-docs://api/dart-io/zlib) → const [ZLibCodec](flutter-docs://api/dart-io/ZLibCodec)
An instance of the default implementation of the [ZLibCodec](flutter-docs://api/dart-io/ZLibCodec).

## Properties

[exitCode](flutter-docs://api/dart-io/exitCode) ↔ [int](flutter-docs://api/dart-core/int)
Get the global exit code for the Dart VM.


[pid](flutter-docs://api/dart-io/pid) → [int](flutter-docs://api/dart-core/int)
Returns the PID of the current process.


[stderr](flutter-docs://api/dart-io/stderr) → [Stdout](flutter-docs://api/dart-io/Stdout)
The standard output stream of errors written by this program.


[stdin](flutter-docs://api/dart-io/stdin) → [Stdin](flutter-docs://api/dart-io/Stdin)
The standard input stream of data read by this program.


[stdout](flutter-docs://api/dart-io/stdout) → [Stdout](flutter-docs://api/dart-io/Stdout)
The standard output stream of data written by this program.


## Functions

[exit](flutter-docs://api/dart-io/exit)([int](flutter-docs://api/dart-core/int) code) → Never
Exit the Dart VM process immediately with the given exit code.

[sleep](flutter-docs://api/dart-io/sleep)([Duration](flutter-docs://api/dart-core/Duration) duration) → void
Sleep for the duration specified in `duration`.

[stdioType](flutter-docs://api/dart-io/stdioType)(dynamic object) → [StdioType](flutter-docs://api/dart-io/StdioType)
Whether a stream is attached to a file, pipe, terminal, or
something else.

## Typedefs

[BadCertificateCallback](flutter-docs://api/dart-io/BadCertificateCallback) = [bool](flutter-docs://api/dart-core/bool) Function([X509Certificate](flutter-docs://api/dart-io/X509Certificate) cr, [String](flutter-docs://api/dart-core/String) host, [int](flutter-docs://api/dart-core/int) port)

## Exceptions / Errors

[CertificateException](flutter-docs://api/dart-io/CertificateException)
An exception that happens in the handshake phase of establishing
a secure network connection, when looking up or verifying a
certificate.

[FileSystemException](flutter-docs://api/dart-io/FileSystemException)
Exception thrown when a file operation fails.

[HandshakeException](flutter-docs://api/dart-io/HandshakeException)
An exception that happens in the handshake phase of establishing
a secure network connection.

[HttpException](flutter-docs://api/dart-io/HttpException)
[IOException](flutter-docs://api/dart-io/IOException)
Base class for all IO related exceptions.

[OSError](flutter-docs://api/dart-io/OSError)
An [Exception](flutter-docs://api/dart-core/Exception) holding information about an error from the
operating system.

[PathAccessException](flutter-docs://api/dart-io/PathAccessException)
Exception thrown when a file operation fails because the necessary access
rights are not available.

[PathExistsException](flutter-docs://api/dart-io/PathExistsException)
Exception thrown when a file operation fails because the target path
already exists.

[PathNotFoundException](flutter-docs://api/dart-io/PathNotFoundException)
Exception thrown when a file operation fails because a file or
directory does not exist.

[ProcessException](flutter-docs://api/dart-io/ProcessException)
[RedirectException](flutter-docs://api/dart-io/RedirectException)
[SignalException](flutter-docs://api/dart-io/SignalException)
[SocketException](flutter-docs://api/dart-io/SocketException)
Exception thrown when a socket operation fails.

[StdinException](flutter-docs://api/dart-io/StdinException)
Exception thrown by some operations of [Stdin](flutter-docs://api/dart-io/Stdin)

[StdoutException](flutter-docs://api/dart-io/StdoutException)
Exception thrown by some operations of [Stdout](flutter-docs://api/dart-io/Stdout)

[TlsException](flutter-docs://api/dart-io/TlsException)
A secure networking exception caused by a failure in the
TLS/SSL protocol.

[WebSocketException](flutter-docs://api/dart-io/WebSocketException)