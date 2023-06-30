import { html } from '../lib.js';
import { hoverModels } from '../scripts/home-models.js';

const homeTmp = () => html`
       <section id="banner">
            <div class="background">
                <img class="background__img"
                    src="https://images.unsplash.com/photo-1501612780327-45045538702b?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1470&q=80"
                    alt="No Image">
                <div class="background__gradient"></div>
            </div>

            <div class="content">
                <div class="headings">
                    <h1 class="content__title "><span class="--highlighted">Sound</span> Sphere</h1>
                    <h2 class="content__subtitle">Surrond yourself with music</h2>
                </div>

                <p class="content__text"><span class="--highlighted">SoundSphere</span> is a cutting-edge sound company
                    that specializes in providing exceptional <span class="--highlighted">audio solutions</span> for a
                    variety of applications. </p>
            </div>
        </section>

        <section id="collaborative-companies">
            <img class="collaborative-companies__logo" src="images/srp-logo.png" alt="No Srp">
            <img class="collaborative-companies__logo" src="images/thebest-logo.png" alt="No TheBest">
            <img class="collaborative-companies__logo" src="images/snoop-logo.png" alt="No Snoop">
            <img class="collaborative-companies__logo" src="images/cashmoney-logo.png" alt="No CashMoney">
            <img class="collaborative-companies__logo" src="images/defjam-logo.png" alt="No DefJam">
        </section>

        <section id="company-aim" class="additional-info">
            <article class="additional-info__article">
                <h1 class="additional-info__title">Why Us?</h1>

                <div class="divider">
                    <div class="divider__left-line"></div>
                    <div class="divider__cut-diamond"></div>
                    <div class="divider__right-line"></div>
                </div>

                <p class="additional-info__content">
                    We take pride in providing a personalized approach to sound, working closely with our clients to
                    understand their vision and goals. Whether you need a sound system for a small gathering or a
                    large-scale production, we have the expertise to make it happen.
                </p>
            </article>
        </section>

        <section id="models">
            <div class="model">
                <img class="model__img"
                    src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=764&q=80"
                    alt="No Image">

                <article class="model__desc">
                    <h2 class="model__desc__title">Jena</h2>
                    <p class="model__desc__text">Content Content Content Content Content Content Content Content Content
                        Content Content Content Content Content Content Content Content Content Content Content Content
                        Content Content Content Content Content Content Content Content Content Content Content Content
                        Content </p>

                    <div class="albums">
                        <h3 class="model__info__title">Albums</h3>

                        <img class="--active"
                            src="https://images.unsplash.com/photo-1679267441399-d73d2640cf68?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxlZGl0b3JpYWwtZmVlZHwzfHx8ZW58MHx8fHw%3D&auto=format&fit=crop&w=500&q=60"
                            alt="No Image">
                        <img src="https://images.unsplash.com/photo-1679267441399-d73d2640cf68?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxlZGl0b3JpYWwtZmVlZHwzfHx8ZW58MHx8fHw%3D&auto=format&fit=crop&w=500&q=60"
                            alt="No Image">
                        <img src="https://images.unsplash.com/photo-1679267441399-d73d2640cf68?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxlZGl0b3JpYWwtZmVlZHwzfHx8ZW58MHx8fHw%3D&auto=format&fit=crop&w=500&q=60"
                            alt="No Image">
                        <img src="https://images.unsplash.com/photo-1679267441399-d73d2640cf68?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxlZGl0b3JpYWwtZmVlZHwzfHx8ZW58MHx8fHw%3D&auto=format&fit=crop&w=500&q=60"
                            alt="No Image">

                        <div class="albums__controls">
                            <i class="control-left fa-sharp fa-solid fa-chevron-left"></i>
                            <i class="control-right fa-sharp fa-solid fa-chevron-right"></i>
                        </div>
                    </div>


                    <div class="media">

                        <ul class="media__list">
                            <li class="media__list__li">
                                <a class="media__list__link" href="">
                                    <i class="fa-brands fa-instagram"></i>
                                </a>
                            </li>
                            <li class="media__list__li">
                                <a class="media__list__link" href="">
                                    <i class="fa-brands fa-facebook"></i>
                                </a>
                            </li>
                            <li class="media__list__li">
                                <a class="media__list__link" href="">
                                    <i class="fa-brands fa-youtube"></i>
                                </a>
                            </li>
                        </ul>
                    </div>
                </article>
            </div>

            <div class="model">
                <img class="model__img"
                    src="https://images.unsplash.com/photo-1539571696357-5a69c17a67c6?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80"
                    alt="No Image">

                <article class="model__desc">
                    <h2 class="model__desc__title">Jena</h2>
                    <p class="model__desc__text">Content Content Content Content Content Content Content Content Content
                        Content Content Content Content Content Content Content Content Content Content Content Content
                        Content Content Content Content Content Content Content Content Content Content Content Content
                        Content </p>

                    <div class="albums">
                        <h3 class="model__info__title">Albums</h3>

                        <img class="--active"
                            src="https://images.unsplash.com/photo-1679267441399-d73d2640cf68?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxlZGl0b3JpYWwtZmVlZHwzfHx8ZW58MHx8fHw%3D&auto=format&fit=crop&w=500&q=60"
                            alt="No Image">
                        <img src="https://images.unsplash.com/photo-1679267441399-d73d2640cf68?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxlZGl0b3JpYWwtZmVlZHwzfHx8ZW58MHx8fHw%3D&auto=format&fit=crop&w=500&q=60"
                            alt="No Image">
                        <img src="https://images.unsplash.com/photo-1679267441399-d73d2640cf68?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxlZGl0b3JpYWwtZmVlZHwzfHx8ZW58MHx8fHw%3D&auto=format&fit=crop&w=500&q=60"
                            alt="No Image">
                        <img src="https://images.unsplash.com/photo-1679267441399-d73d2640cf68?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxlZGl0b3JpYWwtZmVlZHwzfHx8ZW58MHx8fHw%3D&auto=format&fit=crop&w=500&q=60"
                            alt="No Image">

                        <div class="albums__controls">
                            <i class="control-left fa-sharp fa-solid fa-chevron-left"></i>
                            <i class="control-right fa-sharp fa-solid fa-chevron-right"></i>
                        </div>
                    </div>


                    <div class="media">

                        <ul class="media__list">
                            <li class="media__list__li">
                                <a class="media__list__link" href="">
                                    <i class="fa-brands fa-instagram"></i>
                                </a>
                            </li>
                            <li class="media__list__li">
                                <a class="media__list__link" href="">
                                    <i class="fa-brands fa-facebook"></i>
                                </a>
                            </li>
                            <li class="media__list__li">
                                <a class="media__list__link" href="">
                                    <i class="fa-brands fa-youtube"></i>
                                </a>
                            </li>
                        </ul>
                    </div>
                </article>
            </div>

            <div class="model">
                <img class="model__img"
                    src="https://images.unsplash.com/photo-1562572159-4efc207f5aff?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MjB8fG1vZGVsfGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=500&q=60"
                    alt="No Image">

                <article class="model__desc">
                    <h2 class="model__desc__title">Jena</h2>
                    <p class="model__desc__text">Content Content Content Content Content Content Content Content Content
                        Content Content Content Content Content Content Content Content Content Content Content Content
                        Content Content Content Content Content Content Content Content Content Content Content Content
                        Content </p>

                    <div class="albums">
                        <h3 class="model__info__title">Albums</h3>

                        <img class="--active"
                            src="https://images.unsplash.com/photo-1679267441399-d73d2640cf68?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxlZGl0b3JpYWwtZmVlZHwzfHx8ZW58MHx8fHw%3D&auto=format&fit=crop&w=500&q=60"
                            alt="No Image">
                        <img src="https://images.unsplash.com/photo-1679267441399-d73d2640cf68?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxlZGl0b3JpYWwtZmVlZHwzfHx8ZW58MHx8fHw%3D&auto=format&fit=crop&w=500&q=60"
                            alt="No Image">
                        <img src="https://images.unsplash.com/photo-1679267441399-d73d2640cf68?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxlZGl0b3JpYWwtZmVlZHwzfHx8ZW58MHx8fHw%3D&auto=format&fit=crop&w=500&q=60"
                            alt="No Image">
                        <img src="https://images.unsplash.com/photo-1679267441399-d73d2640cf68?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxlZGl0b3JpYWwtZmVlZHwzfHx8ZW58MHx8fHw%3D&auto=format&fit=crop&w=500&q=60"
                            alt="No Image">

                        <div class="albums__controls">
                            <i class="control-left fa-sharp fa-solid fa-chevron-left"></i>
                            <i class="control-right fa-sharp fa-solid fa-chevron-right"></i>
                        </div>
                    </div>


                    <div class="media">

                        <ul class="media__list">
                            <li class="media__list__li">
                                <a class="media__list__link" href="">
                                    <i class="fa-brands fa-instagram"></i>
                                </a>
                            </li>
                            <li class="media__list__li">
                                <a class="media__list__link" href="">
                                    <i class="fa-brands fa-facebook"></i>
                                </a>
                            </li>
                            <li class="media__list__li">
                                <a class="media__list__link" href="">
                                    <i class="fa-brands fa-youtube"></i>
                                </a>
                            </li>
                        </ul>
                    </div>
                </article>
            </div>

            <div class="model">
                <img class="model__img"
                    src="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MjN8fG1vZGVsfGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=500&q=60"
                    alt="No Image">

                <article class="model__desc">
                    <h2 class="model__desc__title">Jena</h2>
                    <p class="model__desc__text">Content Content Content Content Content Content Content Content Content
                        Content Content Content Content Content Content Content Content Content Content Content Content
                        Content Content Content Content Content Content Content Content Content Content Content Content
                        Content </p>

                    <div class="albums">
                        <h3 class="model__info__title">Albums</h3>

                        <img class="--active"
                            src="https://images.unsplash.com/photo-1679267441399-d73d2640cf68?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxlZGl0b3JpYWwtZmVlZHwzfHx8ZW58MHx8fHw%3D&auto=format&fit=crop&w=500&q=60"
                            alt="No Image">
                        <img src="https://images.unsplash.com/photo-1679267441399-d73d2640cf68?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxlZGl0b3JpYWwtZmVlZHwzfHx8ZW58MHx8fHw%3D&auto=format&fit=crop&w=500&q=60"
                            alt="No Image">
                        <img src="https://images.unsplash.com/photo-1679267441399-d73d2640cf68?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxlZGl0b3JpYWwtZmVlZHwzfHx8ZW58MHx8fHw%3D&auto=format&fit=crop&w=500&q=60"
                            alt="No Image">
                        <img src="https://images.unsplash.com/photo-1679267441399-d73d2640cf68?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxlZGl0b3JpYWwtZmVlZHwzfHx8ZW58MHx8fHw%3D&auto=format&fit=crop&w=500&q=60"
                            alt="No Image">

                        <div class="albums__controls">
                            <i class="control-left fa-sharp fa-solid fa-chevron-left"></i>
                            <i class="control-right fa-sharp fa-solid fa-chevron-right"></i>
                        </div>
                    </div>


                    <div class="media">

                        <ul class="media__list">
                            <li class="media__list__li">
                                <a class="media__list__link" href="">
                                    <i class="fa-brands fa-instagram"></i>
                                </a>
                            </li>
                            <li class="media__list__li">
                                <a class="media__list__link" href="">
                                    <i class="fa-brands fa-facebook"></i>
                                </a>
                            </li>
                            <li class="media__list__li">
                                <a class="media__list__link" href="">
                                    <i class="fa-brands fa-youtube"></i>
                                </a>
                            </li>
                        </ul>
                    </div>
                </article>
            </div>

            <div class="model">
                <img class="model__img"
                    src="https://images.unsplash.com/photo-1536924430914-91f9e2041b83?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MzN8fG1vZGVsfGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=500&q=60"
                    alt="No Image">

                <article class="model__desc">
                    <h2 class="model__desc__title">Jena</h2>
                    <p class="model__desc__text">Content Content Content Content Content Content Content Content Content
                        Content Content Content Content Content Content Content Content Content Content Content Content
                        Content Content Content Content Content Content Content Content Content Content Content Content
                        Content </p>

                    <div class="albums">
                        <h3 class="model__info__title">Albums</h3>

                        <img class="--active"
                            src="https://images.unsplash.com/photo-1679267441399-d73d2640cf68?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxlZGl0b3JpYWwtZmVlZHwzfHx8ZW58MHx8fHw%3D&auto=format&fit=crop&w=500&q=60"
                            alt="No Image">
                        <img src="https://images.unsplash.com/photo-1679267441399-d73d2640cf68?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxlZGl0b3JpYWwtZmVlZHwzfHx8ZW58MHx8fHw%3D&auto=format&fit=crop&w=500&q=60"
                            alt="No Image">
                        <img src="https://images.unsplash.com/photo-1679267441399-d73d2640cf68?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxlZGl0b3JpYWwtZmVlZHwzfHx8ZW58MHx8fHw%3D&auto=format&fit=crop&w=500&q=60"
                            alt="No Image">
                        <img src="https://images.unsplash.com/photo-1679267441399-d73d2640cf68?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxlZGl0b3JpYWwtZmVlZHwzfHx8ZW58MHx8fHw%3D&auto=format&fit=crop&w=500&q=60"
                            alt="No Image">

                        <div class="albums__controls">
                            <i class="control-left fa-sharp fa-solid fa-chevron-left"></i>
                            <i class="control-right fa-sharp fa-solid fa-chevron-right"></i>
                        </div>
                    </div>


                    <div class="media">

                        <ul class="media__list">
                            <li class="media__list__li">
                                <a class="media__list__link" href="">
                                    <i class="fa-brands fa-instagram"></i>
                                </a>
                            </li>
                            <li class="media__list__li">
                                <a class="media__list__link" href="">
                                    <i class="fa-brands fa-facebook"></i>
                                </a>
                            </li>
                            <li class="media__list__li">
                                <a class="media__list__link" href="">
                                    <i class="fa-brands fa-youtube"></i>
                                </a>
                            </li>
                        </ul>
                    </div>
                </article>
            </div>

            <div class="model">
                <img class="model__img"
                    src="https://images.unsplash.com/photo-1529139574466-a303027c1d8b?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MjJ8fG1vZGVsfGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=500&q=60"
                    alt="No Image">

                <article class="model__desc">
                    <h2 class="model__desc__title">Jena</h2>
                    <p class="model__desc__text">Content Content Content Content Content Content Content Content Content
                        Content Content Content Content Content Content Content Content Content Content Content Content
                        Content Content Content Content Content Content Content Content Content Content Content Content
                        Content </p>

                    <div class="albums">
                        <h3 class="model__info__title">Albums</h3>

                        <img class="--active"
                            src="https://images.unsplash.com/photo-1679267441399-d73d2640cf68?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxlZGl0b3JpYWwtZmVlZHwzfHx8ZW58MHx8fHw%3D&auto=format&fit=crop&w=500&q=60"
                            alt="No Image">
                        <img src="https://images.unsplash.com/photo-1679267441399-d73d2640cf68?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxlZGl0b3JpYWwtZmVlZHwzfHx8ZW58MHx8fHw%3D&auto=format&fit=crop&w=500&q=60"
                            alt="No Image">
                        <img src="https://images.unsplash.com/photo-1679267441399-d73d2640cf68?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxlZGl0b3JpYWwtZmVlZHwzfHx8ZW58MHx8fHw%3D&auto=format&fit=crop&w=500&q=60"
                            alt="No Image">
                        <img src="https://images.unsplash.com/photo-1679267441399-d73d2640cf68?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxlZGl0b3JpYWwtZmVlZHwzfHx8ZW58MHx8fHw%3D&auto=format&fit=crop&w=500&q=60"
                            alt="No Image">

                        <div class="albums__controls">
                            <i class="control-left fa-sharp fa-solid fa-chevron-left"></i>
                            <i class="control-right fa-sharp fa-solid fa-chevron-right"></i>
                        </div>
                    </div>


                    <div class="media">

                        <ul class="media__list">
                            <li class="media__list__li">
                                <a class="media__list__link" href="">
                                    <i class="fa-brands fa-instagram"></i>
                                </a>
                            </li>
                            <li class="media__list__li">
                                <a class="media__list__link" href="">
                                    <i class="fa-brands fa-facebook"></i>
                                </a>
                            </li>
                            <li class="media__list__li">
                                <a class="media__list__link" href="">
                                    <i class="fa-brands fa-youtube"></i>
                                </a>
                            </li>
                        </ul>
                    </div>
                </article>
            </div>

            <div class="model">
                <img class="model__img"
                    src="https://images.unsplash.com/photo-1564485377539-4af72d1f6a2f?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MTV8fG1vZGVsfGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=500&q=60"
                    alt="No Image">

                <article class="model__desc">
                    <h2 class="model__desc__title">Jena</h2>
                    <p class="model__desc__text">Content Content Content Content Content Content Content Content Content
                        Content Content Content Content Content Content Content Content Content Content Content Content
                        Content Content Content Content Content Content Content Content Content Content Content Content
                        Content </p>

                    <div class="albums">
                        <h3 class="model__info__title">Albums</h3>

                        <img class="--active"
                            src="https://images.unsplash.com/photo-1679267441399-d73d2640cf68?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxlZGl0b3JpYWwtZmVlZHwzfHx8ZW58MHx8fHw%3D&auto=format&fit=crop&w=500&q=3000"
                            alt="No Image">
                        <img src="https://images.unsplash.com/photo-1666919643134-d97687c1826c?ixlib=rb-4.0.3&ixid=M3wxMjA3fDF8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1471&q=3000"
                            alt="No Image">
                        <img src="https://images.unsplash.com/photo-1682685796444-acc2f5c1b7b6?ixlib=rb-4.0.3&ixid=M3wxMjA3fDF8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1470&q=3000"
                            alt="No Image">
                        <img src="https://images.unsplash.com/photo-1452421822248-d4c2b47f0c81?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1074&q=1000"
                            alt="No Image">


                        <div class="albums__controls">
                            <i class="control-left fa-sharp fa-solid fa-chevron-left"></i>
                            <i class="control-right fa-sharp fa-solid fa-chevron-right"></i>
                        </div>
                    </div>


                    <div class="media">

                        <ul class="media__list">
                            <li class="media__list__li">
                                <a class="media__list__link" href="">
                                    <i class="fa-brands fa-instagram"></i>
                                </a>
                            </li>
                            <li class="media__list__li">
                                <a class="media__list__link" href="">
                                    <i class="fa-brands fa-facebook"></i>
                                </a>
                            </li>
                            <li class="media__list__li">
                                <a class="media__list__link" href="">
                                    <i class="fa-brands fa-youtube"></i>
                                </a>
                            </li>
                        </ul>
                    </div>
                </article>
            </div>

        </section>

        <section id="info">
            <article class="info-article --left">

                <img class="info-article__img"
                    src="https://images.unsplash.com/photo-1603190287605-e6ade32fa852?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mjd8fGNvbmNlcnR8ZW58MHx8MHx8&auto=format&fit=crop&w=2000&q=60"
                    alt="No Album">

                <div class="content">
                    <h1 class="content__title">About Us</h1>

                    <div class="divider">
                        <div class="divider__left-line"></div>
                        <div class="divider__cut-diamond"></div>
                        <div class="divider__right-line"></div>
                    </div>

                    <p class="content__paragraph">
                        Sound Sphere is a premier audio company that specializes in providing top-quality sound
                        solutions for various events and occasions. Our team of experienced professionals has been
                        providing high-quality audio services for more than a decade.
                    </p>

                    <br />

                    <p class="content__paragraph">
                        At Sound Sphere, we are committed to providing our clients with the highest level of customer
                        service. Our team takes the time to understand your event's unique requirements, ensuring that
                        we provide you with the best sound solution that meets your needs and budget.
                    </p>

                </div>
            </article>

            <section id="events">
                <div class="event">
                    <h3 class="event__location">London</h3>

                    <div class="event__divider"></div>

                    <table class="event__info">
                        <thead>
                            <th class="event__info__head">Id</th>
                            <th class="event__info__head">Date</th>
                            <th class="event__info__head">Genre</th>
                        </thead>
                        <tbody>
                            <tr class="event__info__row">
                                <td class="event__info__data">#242</td>
                                <td class="event__info__data">27.11.2024</td>
                                <td class="event__info__data">Jazz</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
                <div class="event">
                    <h3 class="event__location">London</h3>

                    <div class="event__divider"></div>

                    <table class="event__info">
                        <thead>
                            <th class="event__info__head">Id</th>
                            <th class="event__info__head">Date</th>
                            <th class="event__info__head">Genre</th>
                        </thead>
                        <tbody>
                            <tr class="event__info__row">
                                <td class="event__info__data">#242</td>
                                <td class="event__info__data">27.11.2024</td>
                                <td class="event__info__data">Jazz</td>
                            </tr>
                        </tbody>
                    </table>
                </div>

                <div class="event">
                    <h3 class="event__location">London</h3>

                    <div class="event__divider"></div>

                    <table class="event__info">
                        <thead>
                            <th class="event__info__head">Id</th>
                            <th class="event__info__head">Date</th>
                            <th class="event__info__head">Genre</th>
                        </thead>
                        <tbody>
                            <tr class="event__info__row">
                                <td class="event__info__data">#242</td>
                                <td class="event__info__data">27.11.2024</td>
                                <td class="event__info__data">Jazz</td>
                            </tr>
                        </tbody>
                    </table>
                </div>

                <div class="event">
                    <h3 class="event__location">London</h3>

                    <div class="event__divider"></div>

                    <table class="event__info">
                        <thead>
                            <th class="event__info__head">Id</th>
                            <th class="event__info__head">Date</th>
                            <th class="event__info__head">Genre</th>
                        </thead>
                        <tbody>
                            <tr class="event__info__row">
                                <td class="event__info__data">#242</td>
                                <td class="event__info__data">27.11.2024</td>
                                <td class="event__info__data">Jazz</td>
                            </tr>
                        </tbody>
                    </table>
                </div>

                <div class="event">
                    <h3 class="event__location">London</h3>

                    <div class="event__divider"></div>

                    <table class="event__info">
                        <thead>
                            <th class="event__info__head">Id</th>
                            <th class="event__info__head">Date</th>
                            <th class="event__info__head">Genre</th>
                        </thead>
                        <tbody>
                            <tr class="event__info__row">
                                <td class="event__info__data">#242</td>
                                <td class="event__info__data">27.11.2024</td>
                                <td class="event__info__data">Jazz</td>
                            </tr>
                        </tbody>
                    </table>
                </div>

            </section>

            <article class="info-article --right">

                <img class="info-article__img"
                    src="https://images.unsplash.com/photo-1516450360452-9312f5e86fc7?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8NDJ8fGNvbmNlcnR8ZW58MHx8MHx8&auto=format&fit=crop&w=2000&q=60"
                    alt="No Album">

                <div class="content">
                    <h1 class="content__title">Live Concerts</h1>

                    <div class="divider">
                        <div class="divider__left-line"></div>
                        <div class="divider__cut-diamond"></div>
                        <div class="divider__right-line"></div>
                    </div>

                    <p class="content__paragraph">
                        At SoundSphere, we understand that music has the power to inspire,
                        motivate, and connect people from all walks of life, and that's why we strive to create
                        exceptional events that cater to diverse tastes and preferences.
                    </p>
                    <br />
                    <p class="content__paragraph">
                        At Sound Sphere, we are committed to providing our clients with the highest level of customer
                        service. Our team takes the time to understand your event's unique requirements, ensuring that
                        we provide you with the best sound solution that meets your needs and budget.
                        sound.
                    </p>

                </div>

            </article>
        </section>
`;

export function homePage(ctx) {
    ctx.render(homeTmp());
    hoverModels();
}

