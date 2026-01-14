#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include <arpa/inet.h>

#define PORT1 12576
#define PORT2 22576
#define BUFFER_SIZE 1024

int main() {
    int sock1, sock2;
    struct sockaddr_in serv_addr;
    char buffer[BUFFER_SIZE] = {0};
    char name_date[BUFFER_SIZE];

    // รับข้อมูลจากคีย์บอร์ด
    printf("Enter your name (First Last) and birthdate (ddmmyyyy): ");
    fgets(name_date, BUFFER_SIZE, stdin);
    name_date[strcspn(name_date, "\n")] = '\0';

    // connect port 12576
    sock1 = socket(AF_INET, SOCK_STREAM, 0);
    serv_addr.sin_family = AF_INET;
    serv_addr.sin_port = htons(PORT1);
    inet_pton(AF_INET, "127.0.0.1", &serv_addr.sin_addr);
    connect(sock1, (struct sockaddr *)&serv_addr, sizeof(serv_addr));

    send(sock1, name_date, strlen(name_date), 0);
    read(sock1, buffer, BUFFER_SIZE);
    printf("Client: received: %s\n", buffer);
    close(sock1);

    // connect port 22576
    memset(buffer, 0, BUFFER_SIZE);
    sock2 = socket(AF_INET, SOCK_STREAM, 0);
    serv_addr.sin_port = htons(PORT2);
    connect(sock2, (struct sockaddr *)&serv_addr, sizeof(serv_addr));

    read(sock2, buffer, BUFFER_SIZE);
    printf("Client: received year (AD): %s\n", buffer);
    send(sock2, "Bye", strlen("Bye"), 0);
    close(sock2);

    return 0;
}
