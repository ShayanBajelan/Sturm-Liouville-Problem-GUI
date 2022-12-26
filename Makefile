CXX = g++
CXXFLAGS = -std=c++20 -Wall -O3 -c 
CLLFLAGS = -std=c++20 -Wall -O3 -fPIC -shared
LXXFLAGS = -std=c++20 -lrungekutta -L.
INC = 
OBJECTS = main.o 
LIBS = librungekutta.dll
TARGET = main

$(TARGET): $(OBJECTS) $(LIBS)
	$(CXX) $(LXXFLAGS) $(OBJECTS) -o $(TARGET) 
main.o: main.cpp rungekutta.h
	$(CXX) $(CXXFLAGS) main.cpp
librungekutta.dll: rungekutta.cpp
	$(CXX) $(CLLFLAGS) rungekutta.cpp -o librungekutta.dll

clean:
	rm -f $(TARGET) $(OBJECTS) $(LIBS)
