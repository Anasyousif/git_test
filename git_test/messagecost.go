package main

func maxMessages(thresh int) int {
	totalCost := 0
	messagesSent := 0

	for i := 0; ; i++ {
		costOfNextMessage := 100 + i
		if totalCost+costOfNextMessage > thresh {
			break
		}
		totalCost += costOfNextMessage
		messagesSent++
	}

	return messagesSent
}