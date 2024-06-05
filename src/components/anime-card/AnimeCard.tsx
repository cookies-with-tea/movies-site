import style from './styles.module.scss'
import cnBind from 'classnames/bind'
import { Icon } from '@/ui'

const cx = cnBind.bind(style)

export const AnimeCard = ({
  // url,
  // rating,
  // status,
  }: any) => {
  return (
    <div className={cx('anime-card')}>
      <div className={cx('anime-card__poster')}>
        <div className={cx('anime-card__poster-img')}>
          <img src={'https://img.yani.tv/posters/big/1519225029.webp'} alt={'111'} />
        </div>

        <div className={cx('anime-card__poster-info')}>
          <div className={cx('anime-card__poster-actions')}>
            <Icon name={'star'}/>

            <Icon name={'share'}/>

            <Icon name={'eye-off'}/>
          </div>

          {/*<div className={cx('anime-card__rating')}>*/}
          {/*  7,6*/}
          {/*</div>*/}
        </div>

      </div>

      <div className={cx('anime-card__title')}>
        Токийский гуль: Перерождение
      </div>
    </div>
  )
}
