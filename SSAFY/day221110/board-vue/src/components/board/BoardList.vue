<template>
  <div>
    <h1 class="underline">SSAFY 게시글 목록</h1>
    <div style="text-align: right">
      <button @click="moveWrite">글작성</button>
    </div>
    <div v-if="articles.length">
      <table id="article-list">
        <colgroup>
          <col style="width: 5%" />
          <col style="width: 65%" />
          <col style="width: 10%" />
          <col style="width: 5%" />
          <col style="width: 15%" />
        </colgroup>
        <thead>
          <tr>
            <th>번호</th>
            <th>제목</th>
            <th>작성자</th>
            <th>조회수</th>
            <th>작성일</th>
          </tr>
        </thead>
        <tbody>
          <board-list-item v-for="article in articles" :key="article.articleno" :article="article"></board-list-item>
        </tbody>
      </table>
    </div>
    <div class="text-center" v-else>게시글이 없습니다.</div>
  </div>
</template>

<script>
import BoardListItem from "@/components/board/BoardListItem";
import http from "@/util/http-common";

export default {
  name: "BoardList",
  components: {
    BoardListItem,
  },
  data() {
    return {
      articles: [],
    };
  },
  created() {
    // 비동기
    // TODO : 글목록 얻기.
    http.get(`/board`)
    // .then
    .then(({data}) => (this.articles = data))
  },
  methods: {
    moveWrite() {
      // 컴포넌트 바꿔치기
      // 현재 router를 boardwrite로 바꾸기
      this.$router.push({ name: "boardwrite"}); // /를 붙이면 /board/write로 해줘야댐. ( 경로 다 붙이기 )
    },
  },
};
</script>

<style></style>
