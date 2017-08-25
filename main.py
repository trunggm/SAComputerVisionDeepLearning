# IMPORTS
from dataset import Dataset
from gridmap_manager import GridMapManager
from detection_connected_component import ConnectedComponent
from tracking_kalman_filter import KalmanFilter
# todo: remove visualization
import visualization

# OBTAIN DATA OF CHOSEN SCENARIO
data = Dataset('/home/simonappel/KITTI/raw/','2011_09_26','0001',range(0,100,1))

# CREATE OBJECTS OF GRIDMAP,DETECTOR,TRACKER
gridmap_manager = GridMapManager()
detector = ConnectedComponent(8)
tracker = KalmanFilter()

# LOOP THROUGH TIME FRAMES
#todo: later replace range by one variable that also goes within dataset
for frame in range(0,2):
    #todo: remove debug prints
    print "-----Frame " + str(frame) + "-----"

    # GRIDMAP
    gridmap_manager.fill_point_cloud_in_grids(data.get_point_cloud(frame))

    # DETECTION
    detector.cluster(gridmap_manager)
    print "Number of objects = " + str(detector.number_of_cluster)

    # TRACKING
    tracker.process(detector.get_objects())
    print "Number of tracks  = " + str(len(tracker.get_tracks()))

    # VISUALIZATION
    visualization.show_steps(gridmap_manager.get_gridmap(),
                             detector.get_labeling())
    visualization.show_boxes(detector.get_objects(),
                             detector.get_labeling())
