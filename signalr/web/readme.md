# SignalR from CosmosDB change feed

This application has the following prerequisites:

- Function App with the SignalR Connection Info input and HTTP output
- Set the *Hub name* parameter in the SignalR input (e.g. iot)
- SignalR messages should be sent as JSON with the following fields: id, device, building, temperature (adjust the field names in index.html if they do not match)
- CosmosDB change feed connected to another Azure Function with CosmosDB input and SignalR output: this function should send a message to SignalR for each received change event; use the same SignalR Hub name as above
- SignalR *target* should be *newMessage*: adjust the target name in index.html if it is different

Notes:
- CosmosDB change feed implies a message is sent whenever a CosmosDB item is changed; editing an existing item is a change as well
- I used a Windows Function App on the Consumption plan (JavaScript/NodeJS)
- Messages are sent to CosmosDB from IoT Hub via a Stream Analytics job; to send the messages, I used the Python script in message-routing/routing-query
- Run index.html on a web server. I used the VS Code Live Server extension
- Adjust the CORS settings on the Function App: if you run index.html on http://localhost:5500 then add this to the *Allowed Origins* list; in addition, also set *Enable Access-Control-Allow-Credentials" (see https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Credentials#:~:text=For%20a%20CORS%20request%20with,re%20opting%20in%20to%20including)


# SignalR with Authentication

Requires the following:
- Host the negotiate endpoint on a Function App and enable Authentication (with Azure AD; Express is fine which creates an app registration in Azure AD automatically)
- Host the index-auth-html on a static website via storage account and add the https://... URL to the Allowed External Redirect URLs in the Authentication section of the Function App



