window.onload = function () {
    document.querySelector("#btn-add").addEventListener("click", function(){
        let listDiv = document.querySelector("#poll-answer-list");

        let divEl = document.createElement("div");
        divEl.setAttribute("class", "poll-answer-item");

        let inputEl = document.createElement("input");
        inputEl.setAttribute("type", "text");
        inputEl.setAttribute("name", "answer");

        let btnEl = document.createElement("button");  // button 태그는 기본 타입이 Submit
        btnEl.setAttribute("type", "button");
        btnEl.setAttribute("class", "button");
        btnEl.appendChild(document.createTextNode("삭제"));

        btnEl.addEventListener("click", function(){
            let parentEL = this.parentElement;
            listDiv.removeChild(parentEL);
        });

        divEl.appendChild(inputEl);
        divEl.appendChild(btnEl);

        document.querySelector("#poll-answer-list").appendChild(divEl);
    });

    // 투표 생성 버튼 클릭 이벤트 리스너
    document.querySelector("#btn-make").addEventListener("click", function(){
        // 질문 칸의 값을 가져오기
        let question = document.querySelector("#question").value;
        
        if(!question) { alert("질문은 반드시 입력하세용 !"); return; }
        
        // input name이 answer인 애들을 모두 가져오기.
        let answers = document.querySelectorAll("[name=answer]");
        
        for (let answer of answers) {
            if(!answer.value) { alert("답변을 입력해주세요 !"); return; }
            
        }
        
        let answerArr = [];
        for (let answer of answers) {
            answerArr.push(answer.value);
        }

        // localStorage에는 key(String), value(String)만 저장할 수 있다.
        localStorage.setItem("question", question);
        // localStorage.setItem("answers", answerArr); // 배열이므로 localStorage에 저장 안 됨.
        localStorage.setItem("answers", JSON.stringify(answerArr));
        console.log(localStorage.getItem("answers"));

        if(confirm("투표 생성 하실??")) {
            opener.location.reload(); // 현재 창을 새로고침하고
            self.close();             // 기존에 열려있던 창을 닫기
        }
    });
};
