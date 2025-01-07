/**
 * @license Highcharts JS v11.4.8 (2024-08-29)
 * @module highcharts/modules/draggable-points
 * @requires highcharts
 *
 * (c) 2009-2024 Torstein Honsi
 *
 * License: www.highcharts.com/license
 */
'use strict';
import Highcharts from '../../Core/Globals.js';
import DraggablePoints from '../../Extensions/DraggablePoints/DraggablePoints.js';
const G = Highcharts;
DraggablePoints.compose(G.Chart, G.Series);
export default Highcharts;