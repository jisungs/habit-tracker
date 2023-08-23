  // HTML 요소들을 가져옵니다.
 var checkboxes = document.querySelectorAll('input[type="checkbox"]');
 var lastCheckbox = checkboxes[checkboxes.length - 1];

 // 마지막 체크 박스의 변경 이벤트를 감지합니다.
 lastCheckbox.addEventListener('change', function() {
   var isChecked = lastCheckbox.checked;

   // 다른 체크 박스들을 선택 상태로 설정합니다.
   checkboxes.forEach(function(checkbox, index) {
     if (index !== checkboxes.length - 1) {
       checkbox.checked = isChecked;
     }
   });
 });


// setTimeout(function(){
//   $('#message').fadeOut('slow')
// }, 4000)


setTimeout(function() {
  var element = document.getElementById('message');
  element.style.transition = 'opacity 0.5s';
  element.style.opacity = '0';
}, 4000);
