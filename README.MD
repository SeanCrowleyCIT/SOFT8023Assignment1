SOFT8023Assignment by Sean Crowley

i) I have employed the singleton design patter in my dictionary class. We only ever need 1 instance of this therefore I felt it was most appropriate.

ii) My plan was to use a factory design pattern for the spelling bee game. The idea would be to have an abstract factory and then make concrete implementation classes this could then be expanded upon later. So for example would could have a game that gives treble points for pangrams or a game that only gives points for five letter words etc. and by using a factory we can add new variations very quickly without having to rewrite any code. The possibilities are endless. However due to a combination of time constraints and difficulties with the proto file I ran out of time.

Compiling Problems

The biggest issue I faced was compiling the .proto files. Whenever I try to run the command found in the lab it does not work:
python -m grpc_tools.protoc -I./protos --python_out=.--grpc_python_out=. spellingBee.proto

Not matter how many variations I use it simply would not compile. I did however manage to find a different command online that did work:
python -m grpc.tools.protoc --proto_path=. --python_out=. --grpc_python_out=. spellingBee.proto

I have had no issue compiling using this command however the syntax is slightly different, I wonder if this is why I have been having soo many issues.

