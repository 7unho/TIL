export default {
    template: `
    <div class="regist_form">
        <label for="isbn">도서번호</label>
        <input type="text" id="isbn" v-model="book.isbn" ref="isbn" readonly /><br />
        <label for="title">도서명</label>
        <input type="text" id="title" v-model="book.title" ref="title" /><br />
        <label for="author">저자</label>
        <input type="text" id="author" v-model="book.author" ref="author" /><br />
        <label for="price">가격</label>
        <input type="number" id="price" v-model="book.price" ref="price" /><br />
        <label for="content">설명</label>
        <br />
        <textarea id="content" name="content" v-model="book.content" ref="content" cols="35" rows="5"></textarea><br />
        <button @click="checkValue">등록</button>
        <button @click="moveList">목록</button>
    </div>
        `,

    data() {
        return {
            book: {
                isbn: "",
                title: "",
                author: "",
                price: "",
                content: "",
            },
        };
      },
      created() {
        // url에서 파라미터정보 얻기.
        const params = new URL(document.location).searchParams;
        const books = JSON.parse(localStorage.getItem("books"));

        for (let i = 0; i < books.length; i++) {
          if (books[i].isbn === params.get("isbn")) {
            this.book = books[i];
          }
        }
        // this.ii=this.book.isbn;
      },
      methods: {
        // 입력값 체크하기 - 체크가 성공하면 modifyBook 호출
        checkValue() {
          // 사용자 입력값 체크하기
          // isbn, 제목, 저자, 가격, 설명이 없을 경우 각 항목에 맞는 메세지를 출력
          if (this.isbn == "") {
            alert("도서번호를 입력해주세요 !");
          } else if (this.title == "") {
            alert("제목을 입력해주세요 !");
          } else if (this.author == "") {
            alert("저자를 입력해주세요 !");
          } else if (this.price == "") {
            alert("가격을 입력해주세요 !");
          } else if (this.content == "") {
            alert("설명을 입력해주세요 !");
          } else {
            this.modifyBook();
          }
        },
        modifyBook() {
          const params = new URL(document.location).searchParams;
          let books = JSON.parse(localStorage.getItem("books"));

          for (let i = 0; i < books.length; i++) {
            if (books[i].isbn === this.book.isbn) {
              // 배열 수정
              this.$set(books, i, this.book);
              // books[i] = this.book;
              //userList[i] = this.user; 가능은 하나 vue에선 위에 코드를 지향
              //                         Vue에서는 virtual DOM을 이용하는데 데이터 바인딩이 잘 안될 수가 있다.
            }
          }

          localStorage.setItem("books", JSON.stringify(books));
          this.moveList();
          alert("수정 완료!");

        },
        moveList() {
          location.href = "list.html";
        }
      },
  };



