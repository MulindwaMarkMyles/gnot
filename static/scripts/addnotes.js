let date = new Date()

let month = date.getMonth() + 1
let day = date.getDate()
let day_name = date.getDay()
let hour = date.getHours()
let minutes = date.getMinutes()

let time_stamp = `Edited on ${day_name}, ${day} ${month} at ${hour}:${minutes}`
let time_input = document.querySelector('.date-time-stamp')

window.onload = () => {
	time_input.innerHTML = time_stamp
	console.log(time_input)
}