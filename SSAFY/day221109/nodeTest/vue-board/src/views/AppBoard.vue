<template>
  <div>
    <h2>Vue를 이용한 게시판</h2>
    <board-list></board-list>
    <board-write></board-write>
    <board-view></board-view>
    <board-modify></board-modify>
    <board-delete></board-delete>
  </div>
</template>

<script>
import BoardList from "@/components/board/BoardList";
import BoardWrite from "@/components/board/BoardWrite";
import BoardView from "@/components/board/BoardView";
import BoardModify from "@/components/board/BoardModify";
import BoardDelete from "@/components/board/BoardDelete";

export default {
  name: "AppBoard",
  components: {
    BoardList,
    BoardWrite,
    BoardView,
    BoardModify,
    BoardDelete,
  },
};
</script>

<style>
.underline {
  display: inline-block;
  background: linear-gradient(180deg, rgba(255, 255, 255, 0) 70%, cyan 30%);
}

input,
textarea,
.view {
  width: 100%;
  padding: 12px 20px;
  margin: 8px 0;
  display: inline-block;
  border: 1px solid #ccc;
  border-radius: 4px;
  box-sizing: border-box;
  color: #787878;
  font-size: medium;
}

label {
  display: inline-block;
  width: 80px;
}

button,
.btn {
  width: 8%;
  background-color: #d0d3d0;
  color: rgb(80, 82, 79);
  padding: 14px 20px;
  margin: 8px 10px;
  border: 1px solid #787878;
  border-radius: 4px;
  font-size: large;
  cursor: pointer;
}

#article-list {
  border-collapse: collapse;
  width: 100%;
}

#article-list thead {
  background-color: #ccc;
  font-weight: bold;
}

#article-list td,
#article-list th {
  text-align: center;
  border-bottom: 1px solid #ddd;
  height: 50px;
}

tr:nth-child(even) {
  background-color: #f2f2f2;
}

.regist {
  padding: 10px;
}

.regist_form {
  border-radius: 5px;
  background-color: #f2f2f2;
  padding: 20px;
}
</style>
