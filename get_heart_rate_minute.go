package main

import (
	"bytes"
	"encoding/json"
	"fmt"
	"io/ioutil"
	"net/http"
)

func main() {
	req, err := http.NewRequest("GET", "https://api.fitbit.com/1/user/-/activities/heart/date/2018-09-01/1d/1min.json", nil)
    	if err != nil {
        	fmt.Println(err)
    	}

	req.Header.Add("Authorization", "Bearer ")

	client := &http.Client{}
    	resp, err := client.Do(req)
    	if err != nil {
        	fmt.Println(err)
    	}
    	defer resp.Body.Close()

    	body, err := ioutil.ReadAll(resp.Body)
    	if err != nil {
        	fmt.Println(err)
    	}

	var decode interface{}
	if err := json.Unmarshal(body, decode); err != nil {
		fmt.Println(err)
		return
	}
	fmt.Println(decode)
}
