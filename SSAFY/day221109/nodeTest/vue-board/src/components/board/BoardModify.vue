<template>
  <div class="regist">
    <h1 class="underline">SSAFY 게시글 수정</h1>
    <div class="regist_form">
      <label for="userid">작성자</label>
      <input type="text" id="userid" v-model="article.userId" ref="userid" /><br />
      <label for="subject">제목</label>
      <input type="text" id="subject" v-model="article.subject" ref="subject" /><br />
      <label for="content">내용</label>
      <br />
      <textarea id="content" v-model="article.content" ref="content" cols="35" rows="5"></textarea><br />
      <button @click="checkValue">수정</button>
      <button @click="moveList">목록</button>
    </div>
  </div>
</template>

<script>
export default {
  name: "BoardModify",
  data() {
    return {
      article: Object,
    };
  },
  methods: {
    // 입력값 체크하기 - 체크가 성공하면 registArticle 호출
    checkValue() {
      // 사용자 입력값 체크하기
      // 작성자아이디, 제목, 내용이 없을 경우 각 항목에 맞는 메세지를 출력
      let err = true;
      let msg = "";
      !this.userid && ((msg = "작성자 입력해주세요"), (err = false), this.$refs.userid.focus());
      err && !this.subject && ((msg = "제목 입력해주세요"), (err = false), this.$refs.subject.focus());
      err && !this.content && ((msg = "내용 입력해주세요"), (err = false), this.$refs.content.focus());

      if (!err) alert(msg);
      // 만약, 내용이 다 입력되어 있다면 registArticle 호출
      else this.modifyArticle();
    },
    modifyArticle() {
      console.log("글수정 하러가자!!!!");
      // 비동기
      // TODO : 글번호에 해당하는 글정보 수정.
    },

    moveList() {
      console.log("글목록 보러가자!!!");
    },
  },
  created() {
    // 비동기
    // TODO : 글번호에 해당하는 글정보 얻기.
    this.article = {
      articleNo: 10,
      userId: "ssafy",
      userName: "안효인",
      subject: "안녕하세요",
      content: "안녕하세요!!!!",
      hit: 10,
      registerTime: "2022-11-08 17:03:15",
    };
  },
};
</script>

<style></style>
