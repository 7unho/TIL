export default {
    template: `
    <div class="regist_form">
        <label for="isbn">도서번호</label>
        <input type="text" id="isbn" v-model="book.isbn" ref="isbn" /><br />
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
    methods: {
        // 입력값 체크하기 - 체크가 성공하면 registBook 호출
        checkValue() {
            // 사용자 입력값 체크하기
            // isbn, 제목, 저자, 가격, 설명이 없을 경우 각 항목에 맞는 메세지를 출력
            if (!this.book.isbn) {
                alert("도서번호를 입력해주세요 !");
                this.$refs.isbn.focus();
            } else if (!this.book.title) {
                alert("제목을 입력해주세요 !");
                this.$refs.title.focus();
            } else if (!this.book.author) {
                alert("저자를 입력해주세요 !");
                this.$refs.author.focus();
            } else if (!this.book.price) {
                alert("가격을 입력해주세요 !");
                this.$refs.price.focus();
            } else if (!this.book.content) {
                alert("설명을 입력해주세요 !");
                this.$refs.content.focus();
            } else {
                this.registBook();
            }
        },

        registBook() {
            // 로컬스토리지에 저장된 데이터 가져오기
            const books = JSON.parse(localStorage.getItem("books"));

            books.push(this.book);
            localStorage.setItem("books", JSON.stringify(books));
            alert("등록 성공 !");
            this.moveList();
        },
        moveList() {
            location.href = "list.html";
        }
    }
};