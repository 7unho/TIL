export default {
    template: `
    <div class="regist">
      <h1 class="underline">SSAFY 도서 정보</h1>
      <div class="regist_form">
        <label for="isbn">도서번호</label>
        <div class="view">{{ book.isbn }}</div>
        <label for="title">도서명</label>
        <div class="view">{{ book.title }}</div>
        <label for="author">저자</label>
        <div class="view">{{ book.author }}</div>
        <label for="price">가격</label>
        <div class="view">{{ numberWithCommas(book.price) }}원</div>
        <label for="content">설명</label>
        <div class="view" v-html="enterToBr(book.content)"></div>
        <div style="padding-top: 15px">
          <a @click="doModify"class="btn">수정</a>
          <a @click="doDelete"class="btn">삭제</a>
          <a href="./list.html" class="btn">목록</a>
        </div>
      </div>
    </div>
    `,
    data: function () {
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
      },
      methods: {
        numberWithCommas(x) {
          return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
        },
        enterToBr(str) {
          // 문자열에 enter값을 <br />로 변경.(html상에서 줄바꿈 처리)
          return str.replace(/(?:\r\n|\r|\n)/g, "<brl />");
        },
        doModify(){
          location.href = "modify.html?isbn=" + this.book.isbn;
        },
        doDelete(){
          let check = confirm("정말 삭제하시겠습니까?");
          if(!check) return;
 
          location.href = "./delete.html?isbn=" + this.book.isbn;
        }
      },
  };
