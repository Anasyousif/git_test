package main

type Analytics struct {
	MessagesTotal     int
	MessagesFailed    int
	MessagesSucceeded int
}

type Message struct {
	Recipient string
	Success   bool
}

func analyzeMessage(analytics *Analytics, msg Message){
	analytics.MessagesTotal ++

	if msg.Success {
		analytics.MessagesSucceeded++
	} else {
		analytics.MessagesFailed++
	}
}
