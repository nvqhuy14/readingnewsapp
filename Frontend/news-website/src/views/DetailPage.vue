<template>
    <header>
        <HomeHeader />
    </header>

    <nav>
        <HomeNavBar :slug=this.section />
    </nav>

    <main>
        <div class="container mt-4 mb-4" style="max-width: 60%">
            <div class="row">
                <div class="col">
                    <h6 class="fw-bold text-uppercase" style="font-family: Dosis">{{ article.category }}</h6>
                </div>
            </div>
            <div class="row mt-4">
                <div class="col">
                    <h1 class="display-3 article-title">{{ article.title }}</h1>
                </div>
            </div>
            <div class="row mt-4" >
                <div class="col">
                    <span>
                        <h4 class="article-description"><em>{{ article.description }}</em></h4>
                    </span>
                </div>
            </div>
            <div class="row my-4 border-bottom">
                <div class="col">
                    <div class="row">
                        <h6 class="col-1">
                            <button class="btn">
                                <font-awesome-icon icon="fa-regular fa-share-from-square" />
                            </button>
                        </h6>
                        <h6 class="col-1">
                            <button class="btn">
                                <font-awesome-icon icon="fa-regular fa-bookmark" />
                            </button>
                        </h6>
                        <h6 class="col-1">
                            <button class="btn" data-bs-toggle="offcanvas" data-bs-target="#offcanvasRight">
                                <font-awesome-icon icon="fa-regular fa-comment" />
                            </button>
                        </h6>

                    </div>
                </div>
                <div class="col">
                    <h6 class="float-end">
                        <div class="fw-bold mb-1" v-if="article.location">{{ article.location }}</div>
                        <div v-else>---</div>
                        {{ handleDate(article.date_posted) }}
                    </h6>
                    
                </div>
            </div>
            <div class="row">
                <div class="col">
                    <span v-html="article.content"></span>
                </div>
            </div>
            <div class="row">
                <div class="col">
                </div>
                <div class="col-md-auto">
                    <h6 class="border rounded p-3">
                        <font-awesome-icon icon="fa-solid fa-feather" />
                        <span class="ms-2">{{ article.author }}</span>
                    </h6>
                </div>
            </div>
            
        </div>

        <!-- Offcanvas -->
        <div class="offcanvas offcanvas-end" tabindex="1000" id="offcanvasRight" aria-labelledby="offcanvasRightLabel">
            <div class="offcanvas-header">
                <h5 class="offcanvas-title" id="offcanvasRightLabel">Ý KIẾN</h5>
                <button type="button" class="btn-close" data-bs-dismiss="offcanvas" aria-label="Close"></button>
            </div>
            <div class="offcanvas-body">
                <div class="input-group">
                    <textarea class="form-control" id="opinion" rows="2" placeholder="Ý kiến của bạn"
                        ref="opinion"></textarea>
                    <button class="btn btn-outline-secondary" type="button" @click="onClick()">Gửi</button>
                </div>
                <br>
                <div class="mx-2" v-for="item in this.comments" :key="item.username">
                    <CommentCard :username=item.username :content=item.content :like=item.like />
                </div>
            </div>
        </div>


    </main>

    <footer>
        <HomeFooter />
    </footer>
</template>
  
<script>
import HomeHeader from '../components/HomeHeader.vue';
import HomeNavBar from '../components/HomeNavBar.vue';
import HomeFooter from '@/components/HomeFooter.vue';
import CommentCard from '@/components/CommentCard.vue';
import { HTTP } from '../api'
import myLib from '@/helpers';

export default {
    name: 'DetailPage',
    components: {
        HomeHeader,
        HomeNavBar,
        HomeFooter,
        CommentCard,
        // NewCard,
    },
    data() {
        return {
            comments: [
                {
                    "username": "Nguyễn Văn A",
                    "content": "She had a terrible habit o comparing her life to others. She realized that their life experiences were completely different than her own and that she saw only what they wanted her to see, but that didn't matter. She still compared herself and yearned for what she thought they had and she didn't.",
                    "like": 10
                },
                {
                    "username": "Nguyễn Văn B",
                    "content": "Matt told her to reach for the stars, but Veronica thought it was the most ridiculous advice she'd ever received. Sure, it had been well-meaning when he said it, but she didn't understand why anyone would want to suggest something that would literally kill you if you actually managed to achieve it.",
                    "like": 6
                },
                {
                    "username": "Nguyễn Văn C",
                    "content": "She glanced up into the sky to watch the clouds taking shape. First, she saw a dog. Next, it was an elephant. Finally, she saw a giant umbrella and at that moment the rain began to pour.",
                    "like": 0
                }
            ],
            article: []
        }
    },
    props: {
        section: { type: String, required: true },
        id: { type: String, required: true },
    },
    methods: {
        onClick() {
            console.log(this.$refs.opinion.value)
        },
        handleDate(str) {
            return myLib.parseDate(str)
        }
    },
    // computed: {
    //     article() {
    //         return articleData
    //     }
    // },
    created() {
        HTTP.get('api/articles/' + this.id  +'/')
            .then(response => {
                this.article = response.data
            })
            .catch(e => {
                console.log(e)
                this.$router.push({ name: 'not-found' })
            })
    },
}
</script>
  
  <!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

.article-title {
    text-align: center;
    font-weight: 600 !important;
    line-height: 80px;
    color: #212529;
    font-family: Playfair Display !important;
}

.article-description {
    width: 100%;
    font-weight: 500 !important;
    color: #212529;
    font-family: Playfair Display !important;
}

span :deep(img) {
    width: 100%;
    /* height: 70%; */
    display: block;
    margin-left: auto;
    margin-right: auto;
}

span :deep(figcaption) {
    text-align: center;
    margin-top: 10px;
}

span :deep(p) {
    font-size: 1.3rem;
    font-family: Roboto;
    line-height: 29px;
    color: #343a40;
}
</style>
  