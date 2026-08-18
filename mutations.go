package main
import "errors"
func deleteIfNecessary(users map[string]user, name string) (deleted bool, err error) {
	usr,exists := users[name]
	if !exists {
		return false,errors.New("not found")
	}

	if !usr.scheduledForDeletion {
		return false,nil
	}

	delete(users,name)
	return true,nil
	
}

type user struct {
	name                 string
	number               int
	scheduledForDeletion bool
}
