import { NavLink } from "react-router-dom"
import style from "./navbar.module.scss"
import cnBind from 'classnames/bind'

const cx = cnBind.bind(style)

export const Navbar = () => {
    // DEBT: до реализации компонента popover данный компонент приостановлен
    const navigation = [
        {name:"Главная", path:"/"},
        {name:"Новинки", path:"/new-anime"},
        {name:"Аниме", path:"/anime"},
        {name:"Топы", path:"/anime-top"},
    ]

    return (
        <nav className={cx("nav")}>
            <ul className={cx("menu")}>
                {
                    navigation.map((item, index) => (
                        <li key={index} className={cx("menu__item")}>
                            <NavLink to={item.path} className={cx("menu__link")}>
                                {item.name}
                            </NavLink>
                        </li>
                    ))
                }
            </ul>
        </nav>
    )
}
