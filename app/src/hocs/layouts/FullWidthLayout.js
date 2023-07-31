import React from 'react'
import { Connect } from 'react-redux'
function FullWidthLayout({children}) {
  return (
    <div>
        {children}
    </div>
  )
}

const mapStateToProps = (state) => ({
})
export default Connect(mapStateToProps,{})(FullWidthLayout)