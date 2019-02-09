package main

import (
	"fmt"
	"sync"
	"time"

	"github.com/globalsign/mgo"
)

type Heartrate struct {
	Datetime time.Time `bson:date`
	Heartrate int `bson:heartrate`
}

func main() {
	fmt.Println("Start Batch.")

	session, _ := mgo.Dial("mongodb://localhost")
	defer session.Close()

	db := session.DB("fitbit")

	wg := sync.WaitGroup{}

	// 0-9
	wg.Add(1)
	go func(wg *sync.WaitGroup) {
		var heartRate = 83
		var num = 10 * 365 * 12 * 60
		var date = time.Date(1987, 6, 7, 0, 0, 0, 0, time.Local)
		for i:=0; i < num; i++ {
			heartrate := Heartrate{date,heartRate}
			col := db.C("heart_rate_minute")
			col.Insert(heartrate)
			date = date.Add(1 * time.Minute)
		}

		wg.Done()
	}(&wg)

	// 10-19
	wg.Add(1)
	go func(wg *sync.WaitGroup) {
		var heartRate = 70
		var num = 10 * 365 * 12 * 60
		var date = time.Date(1997, 6, 7, 0, 0, 0, 0, time.Local)
		for i:=0; i < num; i++ {
			heartrate := Heartrate{date,heartRate}
			col := db.C("heart_rate_minute")
			col.Insert(heartrate)
			date = date.Add(1 * time.Minute)
		}

		wg.Done()
	}(&wg)

	// 20-29
	wg.Add(1)
	go func(wg *sync.WaitGroup) {
		var heartRate = 63
		var num = 10 * 365 * 12 * 60
		var date = time.Date(2007, 6, 7, 0, 0, 0, 0, time.Local)
		for i:=0; i < num; i++ {
			heartrate := Heartrate{date,heartRate}
			col := db.C("heart_rate_minute")
			col.Insert(heartrate)
			date = date.Add(1 * time.Minute)
		}

		wg.Done()
	}(&wg)

	// 30-31(〜8月)
	wg.Add(1)
	go func(wg *sync.WaitGroup) {
		var heartRate = 66
		var num = 10 * 365 * 8 * 60
		var date = time.Date(2017, 6, 7, 0, 0, 0, 0, time.Local)
		for i:=0; i < num; i++ {
			heartrate := Heartrate{date,heartRate}
			col := db.C("heart_rate_minute")
			col.Insert(heartrate)
			date = date.Add(1 * time.Minute)
		}

		wg.Done()
	}(&wg)

	wg.Wait()

	fmt.Println("End Batch.")
}
