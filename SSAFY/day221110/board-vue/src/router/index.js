import Vue from "vue";
import VueRouter from "vue-router";

// lazy loading : 한 번에 import를 해온 후 사용
import AppMain from "@/views/AppMain";
import AppUser from "@/views/AppUser";

// import AppBoard from "@/views/AppBoard";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "main",
    component: AppMain,
  },
  {
    path: "/user",
    name: "user",
    component: AppUser,
  },
  {
    path: "/board",
    name: "board",
    component: () => import("@/views/AppBoard"), // lazy loading과 달리 필요할 때만 import해서 사용함.
    redirect: "/board/list", // /board로 들어오는 경로를 list가 기본이 되게
    children: [              // /board로 들어온 경로의 하위 path mapping
      {
        path: "list", // Mapping("/board/list")
        name: "boardlist",
        component: () => import("@/components/board/BoardList"),
      },
      {
        path: "write", // Mapping("/board/list")
        name: "boardwrite",
        component: () => import("@/components/board/BoardWrite"),
      },

      // 수정, 삭제, 상세정보는 글 번호를 param으로 보내줘야 하므로 :articleno 포함하기
      {
        path: "view/:articleno", // Mapping("/board/list")
        name: "boardView",
        component: () => import("@/components/board/BoardView"),
      },
      {
        path: "modify/:articleno", // Mapping("/board/list")
        name: "boardmodify",
        component: () => import("@/components/board/BoardModify"),
      },
      {
        path: "delete/:articleno", // Mapping("/board/list")
        name: "boarddelete",
        component: () => import("@/components/board/BoardDelete"),
      },
    ],
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
