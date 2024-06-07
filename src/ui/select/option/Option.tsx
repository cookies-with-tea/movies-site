import { OptionType } from '@/types'
import { ReactNode } from 'react'
import style from './styles.module.scss'
import cnBind from 'classnames/bind'

const cx = cnBind.bind(style)

interface OptionsProps {
  option: OptionType
  onChange: (value: OptionType) => void
  checkIconPosition?: 'left' | 'right'
  checkedIcon?: ReactNode | boolean
  isChecked: boolean
}

export const Option = ({
  onChange,
  checkIconPosition = 'right',
  checkedIcon,
  option,
  isChecked
  }: OptionsProps) => {
  return (
    <li
      className={cx('menu__item', checkIconPosition, {
        'menu__item_active': isChecked
      })}
      onClick={() => onChange(option)}
    >
      { option.label }

      { checkIconPosition && isChecked && (
        <div className={cx('menu__item-icon')}>
          { checkedIcon }
        </div>
      ) }
    </li>
  )
}