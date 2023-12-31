<template>
  <v-container style="margin-bottom: 100px; padding-bottom: 100px">
    <v-row>
      <v-col>
        <v-card variant="flat">
          <div
            style="
              margin-top: 10px;
              display: flex;
              justify-content: space-between;
            "
          >
            <div style="margin: 10px; display: flex">
              <v-avatar color="surface-variant" rounded="0" :size="40">
                <v-img
                  src="https://w7.pngwing.com/pngs/188/501/png-transparent-computer-icons-anonymous-anonymity-anonymous-face-monochrome-head-thumbnail.png"
                />
              </v-avatar>
              <div style="margin-left: 10px">
                <p style="font-size: 16px; font-weight: 600">
                  {{ article?.username }}
                </p>
                <p style="font-size: 13px; color: #959595">
                  {{ formatDate(article?.created_at) }}
                </p>
              </div>
            </div>
            <div>
              <v-card-actions v-if="article.user == userInfo">
                <v-btn
                  style="background-color: #f6f7f9"
                  color="#959595"
                  @click="deleteArticle"
                  >삭제</v-btn
                >
              </v-card-actions>
            </div>
          </div>

          <v-card-text style="height: 360px">
            <p
              style="
                font-size: 24px;
                margin-top: 15px;
                margin-bottom: 15px;
                font-weight: 600;
              "
            >
              {{ article?.title }}
            </p>
            <p style="font-size: 18px; margin-top: 30px">
              {{ article?.content }}
            </p>
          </v-card-text>

          <v-card-actions
            variant="flat"
            style="text-align: right"
            v-if="article.user == userInfo"
          >
            <v-btn
              style="background-color: #f6f7f9"
              color="#959595"
              @click="moveUpdate"
              >수정</v-btn
            >
          </v-card-actions>
        </v-card>

        <v-divider></v-divider>

        <v-form @submit.prevent="createComment">
          <v-row
            style="
              display: flex;
              flex-direction: row;
              justify-content: space-between;
              align-items: center;
            "
          >
            <v-col style="width: 300px; margin-top: 13px">
              <v-text-field
                clearable
                variant="outlined"
                v-model="content"
                placeholder="댓글을 입력하세요"
                style="width: 270px; padding-right: 0px; margin-top: 5px"
              ></v-text-field>
            </v-col>

            <v-col style="padding-left: 0px; padding-right: 0px">
              <v-btn
                style="padding-left: 0px; padding-right: 0px"
                size="large"
                variant="text"
                type="submit"
                ><v-icon icon="mdi-send"></v-icon
              ></v-btn>
            </v-col>
          </v-row>
        </v-form>

        <v-divider></v-divider>

        <v-row v-for="comment in article.comments" :key="comment.id">
          <v-col style="margin-top: 10px">
            <p style="font-size: 14px; font-weight: 700">익명</p>
            <p style="font-weight: 400; color: #858585">
              {{ comment.content }}
            </p>

            <v-divider style="margin: 10px" :thickness="1"></v-divider>

            <v-row v-if="comment.user == userInfo">
              <v-col
                style="text-align: right; padding-top: 0px; padding-bottom: 0px"
              >
                <v-btn
                  style="color: #959595"
                  size="small"
                  variant="text"
                  @click="editComment(comment)"
                  >댓글 수정</v-btn
                >
                <v-btn
                  style="color: #959595"
                  size="small"
                  variant="text"
                  @click="deleteComment(comment.id)"
                  >댓글 삭제</v-btn
                >
              </v-col>
            </v-row>

            <v-row v-if="comment.editing">
              <v-col>
                <v-text-field
                  clearable
                  variant="underlined"
                  v-model="comment.editedContent"
                  label="수정 내용"
                ></v-text-field>
                <v-btn
                  style="color: #959595"
                  size="small"
                  variant="text"
                  @click="saveComment(comment)"
                  >저장</v-btn
                >
                <v-btn
                  style="color: #959595"
                  size="small"
                  variant="text"
                  @click="cancelEdit(comment)"
                  >취소</v-btn
                >
              </v-col>
            </v-row>
          </v-col>
        </v-row>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
import axios from "axios";
import { onMounted, ref } from "vue";
import { useRoute, useRouter } from "vue-router";
import { useAccountStore } from "@/stores/account";

const store = useAccountStore();
const route = useRoute();
const router = useRouter();

const article = ref({});
const content = ref("");

// 수정 페이지로 이동
const moveUpdate = () => {
  router.push({ name: "UpdateView", params: { id: article.value.id } });
};

const deleteArticle = () => {
  axios({
    method: "delete",
    url: `${store.API_URL}/api/v1/articles/${route.params.id}/`,
    headers: {
      Authorization: `Token ${store.token}`,
    },
  })
    .then((res) => {
      console.log("삭제 완료");
      router.push({ name: "ArticleView" });
    })
    .catch((err) => {
      console.log(err);
    });
};

// 댓글 생성
const createComment = () => {
  axios({
    method: "post",
    url: `${store.API_URL}/api/v1/articles/${route.params.id}/comments/`,
    data: {
      content: content.value,
    },
    headers: {
      Authorization: `Token ${store.token}`,
    },
  })
    .then((res) => {
      console.log(res.data);
      // router.push({ name: "DetailView" });
      console.log("댓글이 생성되었습니다.");
      if (article.value && Array.isArray(article.value.comments)) {
        article.value.comments.push(res.data);
        article.value = { ...article.value };
      }

      content.value = "";
      console.log(article.value.comment);
    })
    .catch((err) => {
      console.log(err);
    });
};

// 댓글 삭제
const deleteComment = (commentId) => {
  axios({
    method: "delete",
    url: `${store.API_URL}/api/v1/comments/${commentId}/`,
    headers: {
      Authorization: `Token ${store.token}`,
    },
  })
    .then((res) => {
      console.log("댓글 삭제 완료");
      // router.go(); - 이걸 쓰게 되면 새로고침 되면서 삭제됨
      article.value.comments = article.value.comments.filter(
        (comment) => comment.id !== commentId
      );
    })
    .catch((err) => {
      console.log(err);
    });
};

// 댓글 수정
const editComment = (comment) => {
  comment.editing = true;
  comment.originalContent = comment.content;
  comment.editedContent = comment.content;
};

const saveComment = (comment) => {
  axios({
    method: "put",
    url: `${store.API_URL}/api/v1/comments/${comment.id}/`,
    data: {
      content: comment.editedContent,
    },
    headers: {
      Authorization: `Token ${store.token}`,
    },
  })
    .then((res) => {
      console.log("댓글 수정 완료");
      comment.content = comment.editedContent;
      comment.editing = false;
    })
    .catch((err) => {
      console.log(err);
    });
};

const cancelEdit = (comment) => {
  comment.editedContent = comment.originalContent;
  comment.editing = false;
};

// 생성일 수정일을 연,월,일 까지만 나타내도록
const formatDate = (dateString) => {
  const options = { year: "numeric", month: "numeric", day: "numeric" };
  return new Date(dateString).toLocaleDateString("ko-KR", options);
};

const userInfo = ref(null);
onMounted(() => {
  axios({
    method: "GET",
    url: `${store.API_URL}/api/v1/articles/${route.params.id}/`,
  })
    .then((res) => {
      article.value = res.data;
    })
    .catch((err) => {
      console.log(err);
    });

  axios({
    method: "get",
    url: `http://127.0.0.1:8000/accounts/user_info/`,
    headers: {
      Authorization: `Token ${store.token}`,
    },
  })
    .then((res) => {
      userInfo.value = res.data.id;
      // console.log(res.data);
    })
    .catch((err) => {
      console.log(err);
    });
});
</script>

<style scoped></style>
