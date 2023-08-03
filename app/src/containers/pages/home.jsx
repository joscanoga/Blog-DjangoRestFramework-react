import FullWidthLayout from 'hocs/layouts/FullWidthLayout'
import React from 'react'
import { connect } from 'react-redux'
function Home() {
  return (
    <FullWidthLayout>Home</FullWidthLayout>
  )
}
const mapStateToProps = (state) => ({})
export default connect(mapStateToProps,{})(Home)