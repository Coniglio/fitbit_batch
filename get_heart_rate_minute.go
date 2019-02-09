package main

import (
	"fmt"

	"github.com/globalsign/mgo"
)

type Heartrate struct {
	Heartrate int `bson:heartrate`
}

func main() {
	fmt.Println("Start Batch.")

	session, _ := mgo.Dial("mongodb://localhost")
	defer session.Close()
	db := session.DB("fitbit")

	heartrate := Heartrate{60}
	col := db.C("heart_rate_minute")
	err := col.Insert(heartrate)
	if err != nil {
    	fmt.Println("Insert error:", err)
	}

	fmt.Println("End Batch.")
}
