import React from 'react'

function CardID() {

    const generateRandomString = () => {
        const length = 30
        const character = "ABCDEFGHIJK1234567"
        let randomString = ""

        for (let i = 0; i < length; i++) {
            const randomIndex = Math.floor(Math.random() * character.length )
            randomString += character.charAt(randomIndex)

        }
        localStorage.setItem("randomString", randomString)

    }

    const existingRandomString = localStorage.getItem("randomString")
    if (!existingRandomString) {
        generateRandomString()
    }  else {
       
    }
    return existingRandomString

}


export default CardID