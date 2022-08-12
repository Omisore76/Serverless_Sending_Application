function formToApi(event, SendingType) {

    event.preventDefault()

    var data = {
        SendingType: SendingType,
        RecipientEmail: document.getElementsByName('email')[0].value,
        RecipientNumber: document.getElementsByName('sms')[0].value,
        Message: document.getElementsByName('message')[0].value
    }

    fetch( "https://toex53sdmk.execute-api.us-east-1.amazonaws.com/MyStage/myresource" , {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data),
        mode: "no-cors"
    })
}