 type Key struct {

    Path    string

    Country string

}


hits := make(map[Key]int)

hits[Key{Path: "/", Country: "vn"}]++