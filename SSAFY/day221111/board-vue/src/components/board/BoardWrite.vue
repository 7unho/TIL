<template>
    <div>
        <div class="container">
            <b-card bg-variant="light">
                <b-form-group label-cols-lg="3" label="글 작성하기" label-size="lg" label-class="font-weight-bold pt-0"
                    class="mb-0">

                    <b-form-group label="글제목:" label-for="nested-city" label-cols-sm="2" label-align-sm="right">
                        <b-form-input id="input-2" v-model="board.title" type="text" placeholder="글 제목" required>
                        </b-form-input>
                    </b-form-group>

                    <b-form-group label="작성자:" label-for="nested-state" label-cols-sm="2" label-align-sm="right">
                        <b-form-input id="input-3" v-model="board.writer" placeholder="작성자" required></b-form-input>
                    </b-form-group>

                    <b-form-group label="내용:" label-for="nested-country" label-cols-sm="2" label-align-sm="right">
                        <b-form-textarea id="input-4" v-model="board.content" placeholder="내용..." required>
                        </b-form-textarea>
                    </b-form-group>

                    <div style="padding-top: 15px">
                        <b-button @click="newPost" variant="primary">등록</b-button>
                <b-button :to="'/board/list'" variant="danger">취소</b-button>
                    </div>
                    <b-card class="mt-3" header="Form Data Result">
                        <pre class="m-0">{{ board }}</pre>
                    </b-card>
                </b-form-group>
            </b-card>
        </div>
    </div>

</template>
<script>
import http from "@/util/http-common";

export default {
    name: "BoardWrite",
    data() {
        return {
            board: {
                title: "",
                writer: "",
                content: "",
            },
        }
    },
    components: {
    },
    methods: {
        newPost() {
            let board = {
                title: this.board.title,
                writer: this.board.writer,
                content: this.board.content,
            }

            http({
                url: "/board",
                method: "post",
                data: board,
            }).then(({ data }) => {
                let msg = "글 등록 중 문제 발생";

                if (data == 'success') msg = "글 등록 완료 !";
                alert(msg);
                this.$router.push(({ name: "board" }));
            });
        }
    }
}
</script>

<style>

</style>