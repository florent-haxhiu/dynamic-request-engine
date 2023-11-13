package main

import (
	"encoding/json"
	"fmt"
	"log"
	"net/http"
)

func HelloHandler(w http.ResponseWriter, r *http.Request) {
	if r.URL.Path != "/hello" {
		http.Error(w, "Error, path does not exist", http.StatusNotFound)
		return
	}

	if r.Method != "GET" {
		http.Error(w, "Error, Method not supported", http.StatusNotFound)
		return
	}

    res, _ := json.Marshal("Hello User")

    w.Header().Set("Content-Type", "application/json") 

	fmt.Fprintf(w, string(res))
}

func main() {
	http.HandleFunc("/hello", HelloHandler)

	fmt.Println("Server listening on port 8080")
	if err := http.ListenAndServe(":8080", nil); err != nil {
		log.Fatal(err)
	}
}
