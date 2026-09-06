package main

import (
	"fmt"
	"net/http"
)

func deleteUser(baseURL, id, apiKey string) error {
	fullURL := baseURL + "/" + id

	req, err := http.NewRequest("DELETE",fullURL,nil)
	if err != nil {
		return err
	}
	req.Header.Set("X-API-KEY",apiKey)
	res,err := http.DefaultClient.Do(req)
	if err != nil {
		return err
	}
	defer res.Body.Close()

	if res.StatusCode < 200 || res.StatusCode >= 300 {
		return fmt.Errorf("request failed with status code: %d",res.StatusCode)
	}
	return nil
}
