package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"net/http"
	"reflect"
)

func main() {
	req, err := http.NewRequest("GET", "https://api.fitbit.com/1/user/-/activities/heart/date/2018-09-01/1d/1min.json", nil)
    	if err != nil {
        	fmt.Println(err)
    	}

	req.Header.Add("Authorization", "")

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
	errUnmarshal := json.Unmarshal(body, &decode)
	if errUnmarshal != nil {
		fmt.Println("Unmarshal error:", errUnmarshal)
		return
	}

	var activitiesHeart = decode.(map[string]interface{})
	fmt.Println(reflect.TypeOf(activitiesHeart))
	fmt.Println(activitiesHeart)
}
