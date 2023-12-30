import { Outlet } from "react-router-dom"
import style from "./GuestLayout.module.scss"

export const GuestLayout = () => {
    return (
        <div className={style.auth}>
            <div className={style.auth__body}>
                <Outlet/>
            </div>
        </div>
    )
}
