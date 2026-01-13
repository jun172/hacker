CC = gcc
CFLAGS = -Wall -O2 -I modules

TARGET = dosdiag

SRC = main.c \
      modules/syn_flood.c \
      modules/udp_flood.c \
      modules/icmp_flood.c \
      modules/dns_flood.c \
      modules/http_flood.c

OBJ = $(SRC:.c=.o)

$(TARGET): $(OBJ)
	$(CC) $(CFLAGS) -o $(TARGET) $(OBJ)

clean:
	rm -f $(OBJ) $(TARGET)
