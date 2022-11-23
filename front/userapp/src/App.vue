<template>
  <div id="app">
    <img alt="프로필 이미지" :src="getUserProfileImage" />
    <div>
      <h1>Sign UP</h1>
      ID :
      <br />
      <input type="text" v-model="credentials.username" />
      <hr />
      PASSWORD :
      <br />
      <input type="password" v-model="credentials.password" />
      <br />
      PWCONFIRM :
      <br />
      <input type="password" v-model="credentials.passwordConfirm" />
      <hr />
      IMAGE :
      <input type="file" @change="changeImage" />
      <hr />
      <button @click="signUp">SIGN UP</button>
    </div>
    <div>
      <h1>LogIn</h1>
      ID :
      <br />
      <input type="text" v-model="username" />
      <hr />
      PASSWORD :
      <br />
      <input type="password" v-model="password" />
      <hr />
      <button @click="login">LOGIN</button>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import vjd from "vue-jwt-decode";

export default {
  name: "App",
  data() {
    return {
      // 로그인 데이터
      username: "",
      password: "",

      // 회원가입 데이터
      credentials: {
        username: "",
        password: "",
        passwordConfirm: "",
        image: null,
      },

      // 이미지 경로
      userImage: null,
    };
  },
  computed: {
    // 장고 서버에 이미지 media 경로 요청
    getUserProfileImage() {
      return "http://127.0.0.1:8000" + this.userImage;
    },
  },
  methods: {
    // input:file 에는 v-model 을 사용할수 없음.
    changeImage(e) {
      this.credentials.image = e.target.files[0];
    },
    signUp() {
      // 요청에 파일이 포함된 경우 폼데이터로 요청 전송 필요
      let userForm = new FormData();
      userForm.append("username", this.credentials.username);
      userForm.append("password", this.credentials.password);
      userForm.append("passwordConfirm", this.credentials.passwordConfirm);
      userForm.append("image", this.credentials.image);
      console.log(userForm);
      axios({
        method: "post",
        url: "http://127.0.0.1:8000/accounts/signup/",
        data: userForm,
        // 폼 데이터 안에 파일이 포함되어 있으니 헤더 설정 변경
        headers: {
          "Content-Type": "multipart/form-data",
        },
      })
        .then(() => {
          alert("회원가입 성공!");
        })
        .catch((err) => {
          console.log(err);
        });
    },
    login() {
      axios({
        method: "post",
        url: "http://127.0.0.1:8000/api/token/",
        data: {
          username: this.username,
          password: this.password,
        },
      })
        .then((res) => {
          localStorage.setItem("jwt", res.data.access);
          let userId = vjd.decode(res.data.access).user_id;

          axios({
            method: "get",
            url: "http://127.0.0.1:8000/accounts/user/" + userId,
          })
            .then((res) => {
              console.log(res.data);
              this.userImage = res.data.image;
              console.log(this.image);
            })
            .catch((err) => {
              console.log(err);
            });
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
