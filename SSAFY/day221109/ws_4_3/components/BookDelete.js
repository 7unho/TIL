export default {
    template: `
    <div>
        <h1>SSAFY 도서 삭제</h1>
        <div>삭제중...</div>
      </div>
    `,
    data() {
        return {
            // 도서목록을 저장할 배열
            books: []
        };
    },
    created() {
        // localStorage에서 booklist로 저장된 도서 목록을 얻어온다.         
        this.books = JSON.parse(localStorage.getItem("books"));
        setTimeout(this.doDelete, 1000);
    },
    methods: {
        doDelete() {
            const params = new URL(document.location).searchParams;

            for (let i = 0; i < this.books.length; i++) {
                if (this.books[i].isbn === params.get("isbn")) this.$delete(this.books, i);
            }

            localStorage.setItem("books", JSON.stringify(this.books));
            alert("삭제 완료!");
            location.href = "list.html";
        }
    }
};

