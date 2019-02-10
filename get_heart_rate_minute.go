package main

import (
	"bytes"
	"encoding/json"
	"fmt"
	"io/ioutil"
	"net/http"
)

func main() {

	response, err = http.DefaultClient.Do(&http.Request{
		URL:    "https://api.fitbit.com/1/user/-/activities/heart/date/2019-02-09/1d.json",
		Method: "GET",
		Header: http.Header{
			"Content-Type":  {"application/json"},
			"Authorization": {"Bearer " + ""},
		},
	})
	defer response.Body.Close()
	if err != nil {
		fmt.Println(err)
	}

	body, err = ioutil.ReadAll(response.Body)
	if err != nil {
		fmt.Println(err)
	}

	fmt.Println(body)
}
