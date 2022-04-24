var strGET = window.location.search.replace( '?', '');
let send_msg = document.getElementById("send_msg")

// const url = 'http://127.0.0.1:5000/main';
// const data = {
//     group: strGET.split("=")[1],
//     msg: strGET.split("=")[3]
// }
// $.post(url, data, function(data, status){
//     alert('{$data} and status is {$status}')
// });
send_msg.onclick = function() {
    window.location.href=window.location.href.split('?')[0] += '?';
};
let xhr = new XMLHttpRequest();
xhr.open("POST", "https://003b-31-162-27-201.ngrok.io/main");

let data = `{
  "type": "adminpanel",
  "type2": "send_msgs",
  "group": "${strGET.split("=")[1].split("&")[0]}",
  "msg": "${strGET.split("=")[2]}"
}`;

xhr.send(data);